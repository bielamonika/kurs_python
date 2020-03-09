masa = float(input("Podaj swoja wage: "))
wzrost = float(input("Podaj swoj wzrost: "))
BMI = (masa) / (wzrost) ** 2
if BMI < 25:
    status = "w normie"
elif BMI < 25.99:
    status = "nadwaga"
elif BMI < 34.99:
    status = "I stadium otylosci"
else:
    status = "II stadium otylosci"
print("Twoje BMI to: " + str(round(BMI)) + ". Jego status to: {0}".format(status))
