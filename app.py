namn = "leif stefan holmberg"


# for i in range(0,len(namn)):
#     if i == 0 or  namn[i-1] == ' ':
#         namn[i] = namn[i].upper()    
    #if första tecken snpnson eller tecknet innan var mellanslag
    # namn[i] = namn[i].upper()


#tecknetInnan = ''
# for i in range(0,len(namn)):
#     if i == 0 or tecknetInnan == ' ':
#         namn[i] = namn[i].upper()    
#     tecknetInnan = namn[i]
    #if första tecken snpnson eller tecknet innan var mellanslag
    # namn[i] = namn[i].upper()

# DYNAMISK DATASTRUKTUR
# kan växa och krympa
# lägg till en till kund
# en "låda" med många fack i
# for a in range(0,len(MinaBarn)):
#     print(MinaBarn[a])
MinaBarn = ["Fanny", "Josefine", "Oliver"]

if "Kalle" in MinaBarn:
    print("Kalle finns i mina barn")

if "Fanny" in MinaBarn:
    print("Japp")


while True:
    print("1. Skapa nytt barn")
    print("2. Uppdatera barn")
    print("3. Lista alla barn")
    print("4. Sök barn")
    action = input("vad vill du göra:")
    if action == "3":
        print("*** Alla barn ***")
        for barn in MinaBarn:
            print(barn)
    if action == "1":
        print("*** Skapa nytt barn ***")
        namn = input("Ange namn:")
        MinaBarn.append(namn)
    if action == "2":
        nummer = 1 
        for barn in MinaBarn:
            print(f"{nummer} {barn}")
            nummer = nummer + 1
        nummer = int(input("Vilken vill du ändra på:"))
        namn = input("Ange nytt namn:")
        MinaBarn[nummer-1] = namn
    if action == "4":
        print("*** Sök barn ***")

        seekWord = input("Ange vadd du vill söka efter:")
        seekWord = seekWord.lower()
        for barn in MinaBarn:
            if barn.lower().find(seekWord) != -1:
                print(barn)

# barn1 = "Fanny"
# barn2 = "Josefine"
# barn3 = "Oliver"
# barn4 = "Stellan"

# print(barn1)
# print(barn2)
# print(barn3)
# print(barn4)




a = 12
print(f"fsfsdf {a+13}")
fult = "läxa"
fult2 = "grönsaker"
while True:
    txt = input("Skriv in:")
    txt = txt.lower()
    txt = txt.replace(fult, "****")
    txt = txt.replace(fult2, "*********")
    print(txt)




fult = "läxa"
fult2 = "grönsaker"
while True:
    txt = input("Skriv in:")
    txt = txt.lower()
    if txt.find(fult) == -1: # finns inte
        if txt.find(fult2) == -1:
            print(txt)
            continue
    print("Inga fula ord i vår chat")
    break

    # if txt.find(fult) != -1 or txt.find(fult2) != -1:
    #     print("Inga fula ord i vår chat")
    #     break
    #print(txt)


namn = "Stefan"
i = 1
namn = namn.upper()
i = i+1
print(namn)

while True:
    namn = input("Mata in namn")
    #
    cont = input("Vill du fortsätta ja eller nej")
    # if len(cont) < 1:
    #     print("asdfasdfdas")
    cont = cont.upper()
    # nej , Nej, nEJ, NEJ
    if cont == "NEJ":
        break


# string test = "Hej";
# int antal = test.Length;

namn = "Stefan"
print(namn[1])


namn = input("Vad heter du?")
antal = len(namn)
counta = 0
for a in range(0,antal):
    if namn[a] == "a":
        counta = counta + 1
print(f"Du har {counta} a:n i ditt namn!")

#first = namn[0]
#print(f"Ditt namn börjar på {first}")


namn = "Stefan"
namn = namn + " Holmberg" + " " + " heter jag"
antal = len(namn)



namn = "Hejsan"

d = namn[0]







b = 99
namn = input("What's your name?")
#namn = input('What"s your name?')
#namn = input('Vad heter du?')
age = int(input("Hur gammal är du?"))
if age <= 18:
    print("Du är omyndig")
elif namn == "Stefan" and age == 50:  
    print("Du är evigt ung")
else:    
    print("Du är gammal")



tal1 = int(input("Tal 1"))
tal2 = int(input("Tal 2"))
# if(tal1 == tal2){
#     Console.WriteLine("aaa");
#     Console.WriteLine("bbb");
# }
if tal1 == tal2:
    print("Båda talen är lika")
    print("Hej hej")
elif tal1 > tal2:
    print("ja men tal1 är större")    
else:    
    print("hej")    





print("Hello world")
print("2023-11-20")
print(2023-11-20)

# string efternamn = "";
# text   - ""
# float  - 3.14
# int    - 12
namn = input("Vad heter du?")
age = input("Hur gammal är du?")
age = int(age)
age = age + 1
print("Om ett år är du " + str(age) + " år")


print("Du heter " + namn)


