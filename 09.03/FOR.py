txt = "Cos tam cos tam"
for letter in txt:
    print("-",letter)

my_list = ["Ada", "Ruby", "Julia"]
for imiona in my_list:
    print("Hello ",imiona)

for step in range(5):
    print("Krok: ",step)

for step in range(10,50,10):
    print(step)

names = ["Ada", "Ruby", "Julia"]
for step in range(3):
    print(str(step) + " : " + names[step])

password = ""
magic = "hokuspokus"
for num in range(2,10,2):
    password = password + str(num) + magic[num]
    print(password)

