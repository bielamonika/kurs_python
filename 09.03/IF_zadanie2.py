#Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę.
# Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.

liczba1 = int(input("Podaj liczbe calkowita: "))
liczba2 = int(input("Podaj liczbe calkowita: "))
dzialanie = liczba1 + liczba2
if dzialanie > 100:
    print(dzialanie)
else: print("Koniec.")