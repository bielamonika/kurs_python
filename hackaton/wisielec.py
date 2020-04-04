import random
import json

def import_password():
    filename = "words_json.json"
    with open(filename, "r") as read_file:
        data = json.load(read_file)
    category = input("Please choose category (Fruits, Animals, Countries): ")
    word = str(data[category][random.randint(0,8)]).lower()
    return word

def hangman(password):
    letters_left = list(password)
    letters_guessed = []
    runda_max = len(password) + 2
    for characters in password:
        letters_guessed.append("-")
    for runda in range(runda_max):
        if not letters_left:
            break
        else:
            print("Total number of letters: " + str(len(password)) +
                  "\nLetters guessed: " + str(letters_guessed))
            new_letter = input("Your letter: ")
            if new_letter in letters_left:
                letters_left.remove(new_letter)
                for i in range(0, len(password)):
                    if password[i] == new_letter:
                        letters_guessed[i] = new_letter
                        print("WIN!")
            elif new_letter == password:
                break
            else:
                print("LOOSE! " + str(runda_max - runda - 1) + " ROUNDS LEFT.")

    if not letters_left:
        print("YOU WON, THE PASSWORD IS: " + password.upper())
    else:
        print("YOU LOOSE, THE PASSWORD IS: " + password)

hangman(import_password())
