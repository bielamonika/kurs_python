import random
secret_number = random.randint(0,20)
print(secret_number)
zgaduj = int(input("Zgadnij liczbe od 0 do 20: "))
while zgaduj != secret_number:
    zgaduj = input("Zgadnij liczbe od 0 do 20: ")
