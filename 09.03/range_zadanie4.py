liczba = int(input("Podaj liczbe od 1 do 8: "))
if liczba > 8:
    liczba = int(input("Twoja liczba jest wieksza niz 8! Podaj inna liczbe: "))
print(str(liczba) + "!: ")
ciag_liczb = ""
for cyferka in range(1,liczba+1):
    ciag_liczb = ciag_liczb + " * " + str(cyferka)
ciag_liczb = "0" + ciag_liczb + " = " + str(sum(range(0,liczba+1)))
print(ciag_liczb)
print("Silnia z " + str(liczba) + " wynosi " + str(sum(range(0,liczba+1))))