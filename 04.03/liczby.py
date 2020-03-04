cena = 5.04
spalanie = 6.4
dystans = 120
koszt = float((dystans)/100) * cena * spalanie

print(koszt)

cena = float(input('Podaj cene za litr.'))
spalanie = float(input('Podaj spalanie na 100 km.'))
dystans = int(input('Podaj dystans w km.'))/100
koszt = float(dystans) * cena * spalanie
print('Koszt przejazdu wyniesie ' + str(koszt) + ' zl.')