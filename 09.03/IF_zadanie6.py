# Zapytaj użytkownika o numer od 1 do 100,
# jeśli użytkownik zgadnie liczbę ukrytą przez programistę
# wyświetl komunikat “gratulacje!”, w przeciwnym razie wyświetl “pudło!”.

import random

liczba_user = input("Podaj liczbe od 1 do 100: ")
liczba_rl = random.randint(1, 100)
if liczba_user == liczba_rl:
    print("Gratulacje!")
else:
    print("Pudlo!")
