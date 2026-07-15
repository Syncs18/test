
def greeting():
    print("Hallo Hendrik")
    print("schön dass du wieder da bist!")
    print("Viel Spaß beim Programmieren")

greeting()

def trinken(menge):
    a = 0
    while a < menge:
        print("trinken")
        a += 1

trinken(int(input("Menge eingeben: ")))
print(trinken(int(input("Menge eingeben: "))))

def maximum(a, b):
    if a<b:
        return b
    else:
        return a

print(type(maximum(5, 6)))

# Optionale Parameter

def greeting(first_name,mlast_name, academic_title=""):
    if academic_title != "":
        academic_title += " "
    print("Hallo " +academic_title + first_name + " " + mlast_name)
    print("Schön dass du da bist")

greeting("Dan", "Dan")
greeting("Don", "Don", "Dr.")

# Schlüsselwort Parameter

greeting(academic_title="Dr.", first_name="Dan", mlast_name="Dan")

def multiply (number1 , number2, *numbers):
    sum= number1 * number2
    for i in numbers:
        sum *= i
    return sum

multiply(2,3,4,5)

# Reine Schlüsselwortparameter

print("Test",end=", ")
print("siehst du")

print("test", "siehst du", "d", "u", sep="-")

