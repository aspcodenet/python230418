from dataclasses import dataclass

@dataclass
class Customer:
    Member:bool
    Name:str

    def calculatePrice(self, totalPrice):
        rabatt = 0
        if totalPrice >= 5000:
            rabatt = rabatt + ((totalPrice-5000) * 0.01)
        if self.Member:
            rabatt = rabatt + (totalPrice * 0.02)
        if totalPrice > 1000:
            rabatt = rabatt + 100
        return totalPrice - rabatt

