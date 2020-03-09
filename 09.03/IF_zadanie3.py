ocena_user1 = input("Ocen ksiazke w skali od 1 do 10: ")
ocena_user2 = input("Ocen ksiazke w skali od 1 do 10: ")
ocena_user3 = input("Ocen ksiazke w skali od 1 do 10: ")

srednia_ocen = int(ocena_user1)+int(ocena_user2)+int(ocena_user3)/3

if srednia_ocen > 7:
    ocena = "bardzo dobra"
elif srednia_ocen >= 5:
    ocena = "przecietna"
else:
    ocena = "nie warta uwagi"

print("Uzytkownicy ocenili ksiazke jako " + ocena)

