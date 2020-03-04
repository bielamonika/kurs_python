zdanie = input("Podaj zdanie, ktore jest palindromem: ").replace(" ","").casefold()
if zdanie == zdanie[::-1]:
    print("Twoje zdanie jest palindromem, brawo!")
