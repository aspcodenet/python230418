
def IsValidEmail(input):
    if not  '@' in input:
        return False
    lastPoint = input.rfind('.')
    if lastPoint == -1:
        return False
    antalEfter = len(input) - lastPoint -1
    if antalEfter == 2 or antalEfter == 3:
        return True
    return False


print(IsValidEmail("karl.paa@a.s"))
print(IsValidEmail("karl.paa@a.coma"))
print(IsValidEmail("karl.paaa.se"))
print(IsValidEmail("karl.paa@a.com"))
print(IsValidEmail("karl.p@aaa.se"))
