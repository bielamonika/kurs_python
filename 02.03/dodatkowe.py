#ilosc_minut = 365*24*60
#print ("Rok ma "+ str(ilosc_minut)+ ' minut.')

#imie = input("Podaj imie: ")
#wiek = input("Podaj wiek: ")
#print ("UWAGA: Masz na imie "+ imie + ' i masz ' + wiek + ' lat.')

#a,b,c,d = input("Podaj 4 dowolne liczby calkowite: ").split(sep=",")
#suma = int(a)+int(b)+int(c)+int(d)
#print('Suma twoich liczb to: '+ str(suma))

#liczba1,liczba2,liczba3 = input('Podaj trzy liczby pierwsze: ').split(sep=",")
#wynik = (int(liczba1)*int(liczba2))/int(liczba3)
#print('Wynik dzialania to: '+ str(wynik))

#liczba1,liczba2 = input('Podaj dwie liczby: ').split(sep=',')
#dzialanie1 = int(liczba2)//int(liczba1)
#dzialanie2 = int(liczba2)%int(liczba1)
#print('Pierwsza liczba miesci sie w drugiej ' + str(dzialanie1) + ' razy, a reszta z tego dzialania wynosi ' + str(dzialanie2))


lod_w,lod_sz,lod_g = input('Podaj wysokosc, szerokosc oraz glebokosc lodowki w cm: ').split(',')
win_w, win_sz, win_g = input('Podaj wysokosc, szerokosc oraz glebokosc windy w cm: ').split(',')
lod_obj = int(lod_w) * int(lod_sz) * int(lod_g)
win_obj = int(win_g) * int(win_sz) * int(win_w)
wolne = win_obj - lod_obj
print('Lodowka zajmuje ' + str(lod_obj) + ' cm3, w windzie jest ' + str(win_obj) + ' cm3 miejsca.')
print('W windzie pozostanie ' + str(wolne)+ ' cm3 wolnego miejsca.')