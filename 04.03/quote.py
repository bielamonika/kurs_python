quote = "Honesty is the first chapter in the book of wisdom."
ilosc_znakow = len(quote)
srodek = ilosc_znakow//2
print(quote[-7:])
print(quote[:srodek])
print(quote[:-1])
print(quote[srodek::3])
print(quote[::2])
print(quote[::-1])
print(quote.replace("wisdom","friendship"))
