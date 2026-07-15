
# Fallunterscheidungen => if / elif / else

number = int(input("Bitte eine Ganzzahl: "))

if number < 10:
    print("Eingabe kleiner als 10")
elif number < 100:
    print("Eingabe kleiner als 100")
else:
    print("Eingabe größer als 99")

# Bedingte Ausdrücke

bill = 10

tip = float(input("REchnung: " + str(bill)+ " Euro, Wie viel Trinkgeld: " ))

if tip < bill * 0.1:
    print("Vielen Dank!")
else:
    print("Wow, vielen Dank!")

print("Vielen Dank!") if tip < bill * 0.1 else print("Wow, vielen Dank!")

# while-Schleife
counter = 7
while counter < 10:
    print("Das ist eine Ausgabe ...")
    counter += 1

# Schlüsselwörter brek / continue

password = "pa"
user_input = ""
v = 0
while user_input != password and v <= 3:
    user_input = input("Bitte Passwort eingeben")
    v += 3
print("Passwort richtig")

password = "pa"
user_input = ""
v = 0
while user_input != password:
    if v == 3:
        break
    user_input = input("Bitte Passwort eingeben")
    v += 3
print("Passwort richtig")

while True:
    name= input("Nutzer eingeben: ")
    if name!= "user":
        continue
    if user_input == password:
        break
print("Nutzer eingeloggt")

# for-Schleife

for element in [2, 4, 6, 8]:
    print(element)
for el in "Das ist ein String":
    print(el)
for e in range(3, 10, 2):
    print(e)


