txt = "Ala ma kota. Kot ma Ale."
print (txt[:-4])
print (txt[::2])
print(txt.isnumeric())
print(txt.istitle())

txt2 = "Monika"
print(txt2.center(20,"*"))

banan = "banana"
print(banan.count("na"))

#Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7 i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.
word = input("Podaj wyraz o dlugosci wiekszej niz 7: ")
center = len(word)//2
new_word = word[center-1] + word[center] + word[center + 1]
print(new_word)

s1 = input("Podaj wyraz: ")
s2 = input("Podaj drugi wyraz:  ")
center = len(s1)//2
s3 = s1[:center+1] + s2 + s1[center+1:]
print(s3)

