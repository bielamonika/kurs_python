#Utwórz zmienną przechowującą dowolny ciąg znaków.
# Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
#Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.

ciag_znakow = input("Tutaj wpisz dowolny ciag znakow: ")
if len(ciag_znakow) > 5 and ciag_znakow.count("a") > 0:
    print(ciag_znakow.replace("a","z"))