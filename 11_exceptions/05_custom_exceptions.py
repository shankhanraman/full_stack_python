def brew_chai(flavour):
    if flavour not in ["Masala","Ginger","elaichi"]:
        raise ValueError("Unsupported chai flavour....")
    print(f"brewing {flavour} chai...")

brew_chai("mint")