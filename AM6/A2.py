z1 = float(input("1. Zahl eingeben: "))
z2 = float(input("2. Zahl eingeben: "))
while True:
    r = input("Ersten Buchstaben von einer der Grundrechnungsarten: ")

    if r == "a":
        a = round(z1 + z2, 2)
        print(a)
        break
    elif r == "s":
        a = round(z1 - z2, 2)
        print(a)
        break
    elif r == "m":
        a = round(z1 * z2, 2)
        print(a)
        break
    elif r == "d":
        a = round(z1 / z2, 2)
        print(a)
        break
    else:
        print("falsche eingabe")
