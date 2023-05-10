

def GetFizzBuzz(tal):
    if tal % 3 == 0 and tal % 5 == 0:
        return "FizzBuzz"
    if tal % 3 == 0:
        return "Fizz"
    if tal % 5 == 0:
        return "Buzz"
    return str(tal)