
numbers = [3, 7, 12, 1, 37]
print(type(numbers))

names = ["Hendrik", "Janek", "Anna", "Daniel", "Felix", 3, 4.2]
print(names)

root = [numbers,names]
print(root)
print(names[0])
print(names[-2])

names[0] = "Fritz"
print(names[0])
print(names[0:3])
print(names[:4])
print(names[3:])

print(len(names))
names.append(2)
print(names)
names.insert(1, "Marie")
print(names)
names.pop()
print(names)
#names.remove("Hendrik")
print(names)