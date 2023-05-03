from dataclasses import dataclass

class ChristmasPresent:
    Name:str
    Price:float

class Person:
    Name:str
    Presenter = []
    
    def AddPresent(self,present):
        self.Presenter.append(present)
    
    def GetTotal(self):
        summa = 0
        for x in self.Presenter:
            summa = summa + x.Price
        return summa


