def serve_chai(flavour):
    try:
        print(f"Preparaing {flavour} chai ...")
        if  flavour == "unknown":
            raise ValueError("We don't know that flavour")
    except ValueError as e:
        print("Error:", e)
    else:
        print(f"{flavour} chai is served")
    finally:
        print("Next customer please")

serve_chai("Masala")
serve_chai("Unknown")