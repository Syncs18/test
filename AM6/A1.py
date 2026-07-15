for e in range(1, 100):
    if e % 3 == 0 and e % 4 == 0:
        print("Teilbar durch 3 und 4")
    elif e % 3 == 0:
        print ("Teilbar durch 3")
    elif e % 4 == 0:
        print ("Teilbar durch 4")
    else:
        print(e)