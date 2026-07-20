
file = open("A3.txt", "r")

inhalt = file.read()

teilwort = inhalt.split()

laenwort = ""

for wort in teilwort:
    if len(wort) > len(laenwort):
        laenwort = wort


print(laenwort)
