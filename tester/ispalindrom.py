def IsPalindrom(input):
    s = input.replace(" ", "").upper()
    backwards = ""
    for part in s:
        backwards = part + backwards

    return backwards == s


# print(IsPalindrom("Anna"))
# print(IsPalindrom("Ni talar bra latin"))