
file = open("A2", "r", encoding="utf-8")
inhalt = file.read()

file2 = open("A2_2.txt", "w", encoding="utf-8")
file2.write(inhalt)

file.close()
file2.close()