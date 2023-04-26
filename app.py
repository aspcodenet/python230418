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


