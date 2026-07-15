
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
