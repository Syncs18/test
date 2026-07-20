
countries = {}
file = open("example-file.txt", "r")

for line in file.readlines():
    line_splitted = line.split()
    countries[line_splitted[0]] = line_splitted[1]

print(countries)
file.close()

file = open("write-file.txt", "w")

file.writelines(countries)

file.close()



