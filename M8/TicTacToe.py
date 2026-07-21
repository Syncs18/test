import random

field = ["",
         "1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"
         ]
active_player = "X"
run = True
def print_field():
    print(field[7] + "|" + field[8] + "|" + field[9])
    print(field[4] + "|" + field[5] + "|" + field[6])
    print(field[1] + "|" + field[2] + "|" + field[3])

def next_move():
    global run
    while True:
        player_move = int(input("Bitte Feld eingeben: "))
        if player_move == "q":
            run = False
        if player_move >= 1 and player_move <= 9:
            if field[int(player_move)] == "X" or field[int(player_move)] == "O":
                print("Spielfeld ist bereits belegt bitte wiederholen")
            else:
                return player_move
        else:
            print("Eingegebene Zahl muss zwischen 1 und 9 liegen.")
def check_win():
    if field[1] == field[2] == field[3]:
        return field[1]
    if field[4] == field[5] == field[6]:
        return field[4]
    if field[7] == field[8] == field[9]:
        return field[7]
    if field[1] == field[4] == field[7]:
        return field[1]
    if field[2] == field[5] == field[8]:
        return field[2]
    if field[3] == field[6] == field[9]:
        return field[3]
    if field[1] == field[5] == field[9]:
        return field[1]
    if field[3] == field[5] == field[7]:
        return field[3]

def checkdraw():
    if field[1] != "1" and field[2] != "2" and field[3] != "3" and field[4] != "4" and field[5] != "5" and field[6] != "6" and field[7] != "7" and field[8] != "8" and field[9] != "9":
        return True


def change_player():
    global active_player
    if active_player == "X":
        active_player = "O"
    else:
        active_player = "X"

def rndstart():
    n1 = input("Nummer 1 Bitte geben Sie eine Zahl zwischen 1 und 100 ein (Zahlenspektrum optional):")
    n2 = input("Nummer 2 Bitte geben Sie eine andere Zahl zwischen 1 und 100 ein (Zahlenspektrum optional):")
    zz = random.randint(1, 100)
    u1 = zz - int(n1)
    u2 = zz - int(n2)
    if u1 < 0:
        u1 *= -1
    if u2 < 0:
        u2 *= -1
    if u1 > 0 and u2 > 0:
        if u1 < u2:
            print("Nummer 1 Sie fangen an als Spieler: X")
        elif u2 < u1:
            print("Nummer 2 Sie fangen an als Spieler: X")
        else:
            if zz % 2 == 0:
                print("Nummer 2 Sie fangen an als Spieler: X")
            else:
                print("Nummer 1 Bitte geben Sie eine Zahl zwischen 1 und 100 ein (Zahlenspektrum optional):")

rndstart()

while run:

    print_field()
    player_move = next_move()
    field[int(player_move)] = active_player

    winner = check_win()
    if check_win():
        print("Spieler " + str(winner)+ " hat gewonnen")
        run = False
    elif check_win():
        print("Unentschieden")
        run = False
    change_player()

