from dataclasses import dataclass


@dataclass
class Team:
    Namn:str=""
    FoundedYear:int=0
    Player = []

class Player:
    Namn:str=""
    Age:int=0



@dataclass
class Rectangle:
    Width: int = 0
    Height: int = 0

    def calculateArea(self):
        return self.Width * self.Height


r = Rectangle()    
r.Width = 20
r.Height = 10
x = r.calculateArea()
print(x)

r2 = Rectangle()    
r2.Width = 10
r2.Height = 30
x = r2.calculateArea()
print(x)





@dataclass
class Rectangle:
    Width: int = 0
    Height: int = 0

def calculateArea(rect):
    area = rect.Width * rect.Height
    return area

# r2 = Rectangle()    
# r2.Width = 10
# r2.Height = 3
# print(calculateArea(r2))



@dataclass 
class Person:
    Name: str
    StreetAddress:str = ""
    PostalCode:int = 0
    City: str = ""
    Age:int = 0

    def SetAge(self,newAge):
        if newAge >= 0 and newAge <= 140:
            self.Age = newAge

    def MoveTo(self,gatuAdr, postal,city):
        self.StreetAddress = gatuAdr
        self.City = city
        self.PostalCode = postal

p = Person("Stefan")
p.MoveTo("Testgatan 12",11122,"Teststad")
p.SetAge(50)

# p.StreetAddress = "Testgatan 123"
# p.City = "Teststad"
print(f"{p.Name}")

















# p = Person()    
# p.Name = "Stefan"


# @dataclass
# class HouseBluePrint:
#     Color : str = ""
#     NrOfWindows: int = 0
#     Address: str = ""

# mittHus = HouseBluePrint()
# mittHus.Color = "Brown"
# mittHus.NrOfWindows = 12
# mittHus.Address = "Testgatan 12" 

# syrransHus = HouseBluePrint()
# syrransHus.Color = "Rött"
# syrransHus.NrOfWindows = 9
# syrransHus.Address = "Testgatan 13"
# print("Hello")

