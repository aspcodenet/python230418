def IsPalindrom(input):
    s = input.replace(" ", "").lower()
    backwards = ""
    for part in s:
        backwards = part + backwards

    return backwards == s


print(IsPalindrom("Hejsan"))
print(IsPalindrom("Anna"))
print(IsPalindrom("Ni talar bra latin"))