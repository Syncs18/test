
first_names = ["Max", "Fritz", "Anna"]
last_names = ["Mustermann", "Huber", "Neumann"]
eingabe = input("Auswahl von 0 bis 2: ")
if eingabe == "0":
    print(first_names[0], last_names[0])
elif eingabe == "1":
    print(first_names[1], last_names[1])
elif eingabe == "2":
    print(first_names[2], last_names[2])
else:
    print("falsche Eingabe")