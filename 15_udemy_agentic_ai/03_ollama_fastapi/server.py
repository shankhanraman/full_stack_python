from fastapi import FastAPI,Path,HTTPException,Query
import json
app = FastAPI()

def loadpatients():
    with open("patients.json", "r") as file:
        patients = json.load(file)
    return patients

@app.get("/view")
def getpatients():
    data = loadpatients()
    return data

@app.get("/")
def hello():
    return {"message": "Hello, World!"}

@app.get("/contact-us")
def red_root():
    return {"email":"2101020810@cgu-odisha.ac.in"}
@app.get("/about")
def about():
    return {"message": "Patient Managemnet System API"}

@app.get("/view/{patient_id}")
def view_patient(patient_id: str = Path(..., description="The ID of the patient to retrieve", example="P001")):
    data = loadpatients()
    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code=404, detail="Patient not found")    
    
# HTTP status codes are 3 digits codes returned by a web server to indicate the reult of a clients request 
# They are 2xx, 3xx , 4xx , 5xx

# 2xx success
# 3xx redirection 
# 4xx client error
# 5xx server error

# 200 OK after a GET or POST request
# 201 Created after a POST request that creates a resource
# 204 No Content after a DELETE request
# 400 Bad Request when the client sends invalid data
# 401 Unauthorized when authentication is required
# 403 Forbidden when the client does not have permission to access a resource
# 404 Not Found when a resource is not found
# 500 Internal Server Error when the server encounters an error
# 502 Bad Gateway when the server is acting as a gateway and receives an invalid response
# 503 Service Unavailable when the server is temporarily unavailable

@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height ,weight or bmi'), order: str = Query('asc', description='Order can be asc or desc')):
    valid_fields =['height','weight','bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort_by field. Must be one of {valid_fields}")
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400, detail="Invalid order. Must be 'asc' or 'desc'")
    data = loadpatients()
    sort_order = True if order == 'desc' else False
    sorted_data = dict(sorted(data.items(), key=lambda item: item[1][sort_by], reverse=(order=='desc')))
    return sorted_data

