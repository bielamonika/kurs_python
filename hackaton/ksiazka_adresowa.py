address_book = {
    "Anna Kowalska" : "Modrzewiowa 3, Krakow",
    "Jan Nowak" : "Sloneczna 123a, Warszawa",
    "Martyna Literka" : "Adresowa 154, Tulibrodziwo"
}

def address_display():
    for entry in address_book:
        print(str(entry) + ": " + address_book.get(entry))

def address_insert():
    person = input("Insert name and surname: ")
    while person in address_book:
        print("There is already such person in the address book. Try again.")
        person = input("Insert name and surname: ")
    address = input("Insert address with a house number: ") + ", " + input("Insert city: ")
    address_book[person] = address
    address_display()

def address_remove():
    person = input("Insert a person to be removed: ")
    while person not in address_book:
        print("There is no such entry in the address book. Try again.")
        person = input("Insert a person to be removed: ")
    del address_book[person]
    address_display()

def address_book_actions():
    action = "*" * 8 + "\nWelcome to the address book. \n- insert DISPLAY to display existing entries,"
    action += "\n- insert ADD to add a new entry,"
    action += "\n- insert REMOVE to delete an entry,"
    action += "\n- insert EXIT to terminate the program.\n"
    decision = ""
    while decision != "EXIT":
        decision = input(action)
        if decision == "ADD":
            address_insert()
        elif decision == "REMOVE":
            address_remove()
        elif decision == "DISPLAY":
            address_display()
        elif decision != "EXIT":
            print("Incorrect input. Please try again.")

address_book_actions()



