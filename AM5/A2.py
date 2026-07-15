grose = input("Gib die Größe in Meter an: ")
gewicht = input("Gib das Gewicht in Kilo an: ")

bmi = float(gewicht) / float(grose)**2
bmir = round(bmi, 2)
print("Ihr BMI-Wert liegt bei: ", bmir)
if bmir < 18.5:
    print("Untergewicht")
elif 18.5 >= bmir <= 25:
    print("Normalgewicht")
else:
    print("Übergewicht")
