s1 = input("Podaj wyraz: ")
s2 = input("Podaj drugi wyraz:  ")
center = len(s1)//2
s3 = s1[:center] + s2 + s1[center:]
print(s3)