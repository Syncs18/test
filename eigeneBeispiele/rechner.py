def addieren(*zahlen):
    summe = 0
    for z in zahlen:
        summe += z
    return summe

print("Einfacher taschenrechner")
stelle = 0
stellen = int(input("Wie viele Zahlen gibst du ein"))
zahlen_list = []
while stelle != stellen:
    eingabe = input()
    zahlen_list.append(float(eingabe))
    stelle += 1
ergebnis = addieren(*zahlen_list)
ergebnisr = round(ergebnis, 2)
print("Das Ergebnis ist:", ergebnisr)

