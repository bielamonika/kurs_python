#Napisz grę - kamień (k) / papier (p) / nożyce (n)

import random
figury = ["kamien", "papier", "nozyce"]

remis = 0
komputer = 0
user = 0
runda = 0
figura_user = ""

while figura_user != "koniec":
    figura_user = input("Podaj jedna z trzech figur: kamien, papier lub nozyce: ")
    figura_PC = random.choice(figury)
    if figura_user == "kamien":
        if figura_PC == "kamien":
            print("REMIS")
            remis +=1
        elif figura_PC == "papier":
            print("PRZEGRALES")
            komputer +=1
        else:
            print("WYGRALES")
            user+=1
    elif figura_user == "nozyce":
        if figura_PC == "kamien":
            print("PRZEGRALES")
            komputer+=1
        elif figura_PC == "papier":
            print("WYGRALES")
            user+=1
        else:
            print("REMIS")
            remis+=1
    elif figura_user == "papier":
        if figura_PC == "kamien":
            print("WYGRALES")
            user+=1
        elif figura_PC == "papier":
            print("REMIS")
            remis+=1
        else:
            print("PRZEGRALES")
            komputer+=1
    elif figura_user == "koniec":
        break
    runda+=1
    print("Wynik gracza: " + str(user) + ", wynik komputera: " + str(komputer)+ ". Ilosc rund: " + str(runda))