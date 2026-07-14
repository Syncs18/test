import random
import string


user_l = input("Gib die länge des Passwortes an: ")

pool = (string.ascii_letters + string.digits + string.punctuation)
passwort = ""
for x in range(int(user_l)):
    passwort += random.choice(pool)
print(passwort)