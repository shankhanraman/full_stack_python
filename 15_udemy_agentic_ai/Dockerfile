# Base image
FROM python:3.13.8-alpine

# Set working directory inside container
WORKDIR /main

# Copy requirements file
COPY requirements.txt .

# Install dependencies (fixed typo: --no-cache-dir)
RUN pip install --no-cache-dir -r requirements.txt

# Copy all other files
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Start the app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]