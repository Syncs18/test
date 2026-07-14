groesse = float(input("Größe in Meter: "))
gewicht = float(input("Gewicht in Kilo: "))

bmi = gewicht / (groesse**2)
bmiround = round(bmi, 2)

print("BMI-Wert liegt bei: ")
print(bmiround)

if bmi < 18.5:
    print("untergewicht")
elif bmi <= 18.5 and bmi < 25:
    print("normalgewicht")
else:
    print("übergewicht")