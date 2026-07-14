

minzahl = float(input("Minimalzahl: "))
maxzahl = float(input("Maximzahl: "))
versuche = 0

while True:
    ratezahl = (minzahl + maxzahl) // 2
    versuche += 1
    print("Schätzung:  ")
    print(ratezahl)
    pruf = input("r = richtig, n = zu niedrig, h = zu hoch")

    if pruf == "r":
        print("Fertig")
        print(versuche)
        break
    elif pruf == "n":
        minzahl = ratezahl + 1
    elif pruf == "h":
        maxzahl = ratezahl - 1
    else:
        print("Falsche eingabe")
        versuche -= 1
