password = input("Podaj haslo: ")
haslo = "true"
if len(password) < 8:
    print("Haslo powinno zawierac 8 lub wiecej znakow!")
    haslo = "false"
if password.isdigit() or password.isalpha():
    print("W hasle powinny znadjowac sie zarowno liczby jak i litery!")
    haslo = "false"
if password.islower():
    print("Haslo powinno zawierac conajmniej jedna wielka litere!")
    haslo = "false"
if haslo == "false":
    print("Sprobuj jeszcze raz.")
else:
    print("Super haslo.")
