import datetime
def calculatePrice(price, isPensionar):
    if isPensionar and datetime.datetime.now().weekday == 1:
        return price * 0.98
    return price


