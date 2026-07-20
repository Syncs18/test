
zaelwort = open("A1.txt", "r", encoding="utf-8")

inhalt = zaelwort.read()
anzahl = len(inhalt.split())
print(anzahl)
