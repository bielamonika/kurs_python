#Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.
# Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.

liczba1 = int(input("Podaj pierwsza liczbe: "))
liczba2 = int(input("Podaj druga liczbe: "))
liczba3 = int(input("Podaj trzecia liczbe: "))

hello = [liczba1, liczba2, liczba3]
hello.sort(reverse=True)
print(hello[0])

if liczba1 > liczba2 and liczba1 > liczba3:
    if liczba2 > liczba3:
        print(liczba1,liczba2,liczba3)
    else:
        print(liczba1,liczba3,liczba2)
elif liczba2> liczba1 and liczba2>liczba3:
    if liczba1 > liczba3:
        print(liczba2,liczba1,liczba3)
    else:
        print(liczba2,liczba3,liczba1)
else:
    if liczba2> liczba1:
        print(liczba3,liczba2,liczba1)
    else:
        print(liczba3,liczba1,liczba2)