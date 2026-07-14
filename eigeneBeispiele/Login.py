
print("Benutzer anlegen")
rbenutzer = input("Benutzername: ")
rpasswort = input("Passwort: ")
versuch = 0

while True:
    print("Das ist der login")
    lbenutzer = input("Benutzername: ")
    lpasswort = input("Passwort: ")
    versuch += 1
    if versuch > 1:
        print("zu viele Fehlversuche")
        break
    elif lbenutzer == rbenutzer:
        if lpasswort == rpasswort:
            print("Logged in")
            break
        elif lpasswort != rpasswort:
            print("Benutzer oder Passwort falsch")
    elif lbenutzer != rbenutzer:
        print("Benutzer oder Passwort falsch")

