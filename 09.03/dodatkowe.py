#zadanie1
sentence = "Kurs Pythona jest prosty i przyjemny. "
print(len(sentence))
print(sentence[18:24])
print(sentence[7])
print(sentence[12])
print(sentence[37])
print(sentence[-4])
print(sentence[0]+"ó"+sentence[2:28]+"sz"+sentence[30:])
#zadanie2
imie = input("Podaj swoje imie: ")
nazwisko = input("Podaj swoje nazwisko: ")
nr_tel = str(input("Podaj swoj numer telefonu: "))
imie.isalpha()
nazwisko.isalpha()
nr_tel.isdigit()
imie = imie.title()
nazwisko = nazwisko.title()
if imie[-1] == "a":
    plec = "kobieta"
else:
    plec = "mezczyzna"
nr_tel = nr_tel.replace(" ","")
nr_tel = nr_tel.replace("-","")
personal = imie + " " + nazwisko + " " + nr_tel +" "+ plec
print(len(personal.replace(" ","")))
print(personal)

