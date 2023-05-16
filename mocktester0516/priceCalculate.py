import datetime

def calculatePrice(belopp, isPensionar):
    # om aktuell dag är tisdag så 2 % rabatt
    # skicka tillbaka nya priset
    currentDateAndTime = datetime.datetime.now()
    weekDay = currentDateAndTime.weekday()
    if weekDay == 1 and isPensionar == True: 
        return belopp * 0.98
    return belopp

# x = calculatePrice(100, True)
# print(x)