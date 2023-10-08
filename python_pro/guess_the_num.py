import random
import platform
import os
def clear():
    if platform.system == "Linux":
        os.system("clear")
    elif platform.system == "windows":
        os.system('cls')
print("Welcome to the 'Guess the Number' Game.")
print("You will be guessing the number between 1 to 100.")
x = random.randint(0,100)
def easy(count):
    while count != 0:
        user_input = int(input("Make a Guess:\n"))
        if user_input < x:
            print("too low")
            count -= 1
            print(f"You have {count} chances left to guess")
        elif user_input > x:
            print("too high")
            count -= 1
            print(f"You have {count} chances left to guess")
        elif user_input == x:
            print("You Guessed the right number")
            break
        else:
            print("invalid input, please enter numbers only")
    print("Sorry! all attempts are over. You lose")

def hard(count):
    while count != 0:
        user_input = int(input("Make a Guess:\n"))
        if user_input < x:
            print("too low")
            count -= 1
            print(f"You have {count} chances left to guess")
        elif user_input > x:
            print("too high")
            count -= 1
            print(f"You have {count} chances left to guess")
        elif user_input == x:
            print("You Guessed the right number")
            break
        else:
            print("invalid input, please enter numbers only")
    print("Sorry! all attempts are over. You lose")

while True:
    user_choice = input("Choose the Difficulty. Type 'Easy' or 'Hard', or if want to exit, Type 'Exit': ").lower()
    if user_choice == "hard":
        hard(count = 5)
    elif user_choice == "easy":
        easy(count = 10)
    elif user_choice == "exit":
        False
        break
    else:
        print("Please select the difficulty level properly")