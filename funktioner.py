# FUNKTIONER
# vad avgör om ni får köpa öl?
# (spec) 


def menu():
    print("1. Skapa")
    print("2. Ändra")
    print("3. Avsluta")


menu()    


# ålder      18      20
# location Krogen Systemet
# promilleHalt < 1.0
def canIBuyBeer(age,location,promilleHalt):
    if promilleHalt > 1.0:
        return False
    if location == "S" and age < 19:
        return False
    if location == "K" and age < 18:
        return False
    return True

while True:
    age = int(input("Ange ålder:"))
    location = input("Ange var du är S/K")
    promilleHalt = float(input("Ange din promille:"))
    ok = canIBuyBeer(age,location,promilleHalt)
    if ok  == True:
        print("yes")
    else:
        print("No")    






def enterAge():
    while True:
        age1 = int(input("Ange ålder"))
        if age1 < 0 or age1 > 120 :
            print("Felaktig ålder")
        else:
            break

print("df")
enterAge()

while True:
    age2 = int(input("Ange ålder"))
    if age1 < 0:
        print("Ogiltig")
    else:
        break


def calcVat(price):
    return price * 0.25

pris = 12
pris = calcVat(pris)
print(pris)

# x = 12
# x = x * 0.25
# print(x)








