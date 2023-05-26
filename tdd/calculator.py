
def canIBuyBeer(age,location,promilleHalt):
    if promilleHalt >= 1.0:
        return False

    if age >= 20 and location == "Systemet":
        return True
    if age >= 18 and location == "Krogen":
        return True

    return True