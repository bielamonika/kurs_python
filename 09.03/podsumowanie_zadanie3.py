ciag_znakow = input("Podaj dowolny ciag znakow: ")

m_litery = 0
d_litery = 0
cyfry = 0
znaki_spec = 0

for znak in ciag_znakow:
    if znak.islower() == True:
        m_litery += 1
    elif znak.isupper() == True:
        d_litery += 1
    elif znak.isdigit() == True:
        cyfry += 1
    else:
        znaki_spec += 1
print(m_litery)
print(d_litery)
print(cyfry)
print(znaki_spec)
