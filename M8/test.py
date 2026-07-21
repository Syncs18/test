import random

zahl = input("Zahl: ")
zzahl = 10
minus = zzahl - int(zahl)
print(minus)
if minus < 0:
    minus *= -1
    print(minus)
else:
    print(minus)