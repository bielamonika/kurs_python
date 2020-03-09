ciag_znakow = input("Podaj dowolny ciag znakow: ")
print(ciag_znakow[1::2])
i: int=1
for letter in ciag_znakow:
    if i%2 == 0:
        print(letter)
    i+=1