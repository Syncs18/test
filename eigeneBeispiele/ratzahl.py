import random

vzahl = random.randint(1,100)

print("es ist eine Zahl zwischen 1 bis 100")
versuche = 0

while True:
    versuch = int(input("rate mal:"))
    versuche += 1
    if versuch == vzahl:
        print("richtig")
        print("versuche:", versuche)
        break
    elif versuch < vzahl:
        print("zu klein")
    else:
        print("zu groß")