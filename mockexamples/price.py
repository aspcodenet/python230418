import datetime
def calculatePrice(price, isPensionar):
    day = datetime.datetime.now()
    if isPensionar and day.weekday() == 1:
        return price * 0.98
    return price


