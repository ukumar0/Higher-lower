import game_data as gd
import art
import random
import os
import platform
from art import logo, vs

def clear():
  if platform.system == "windows":
    os.system("cls")
  elif platform.system == "Linux":
    os.system("clear")
print(logo)
score = 0

def user_score():
  global score
  score += 1

pointer = gd.data
#Creating a function for random selection from the data for comparison of value entered with values in the dictionaries stored.

def compare():
  compA = random.choice(pointer)
  print("compare A: ", end='')
  #Taking the index value and printing it to the terminal
  for key, value in enumerate(compA):
    if key == 0:
      print(f"{compA[value]}, ", end='')
    elif key == 2:
      print(f"a {compA[value]}, ", end='')
    elif key == 1:
      coin1 = compA[value]
    elif key == 3:
      print(f"from {compA[value]}.")
  print(vs)
  compB = random.choice(pointer)
  print("compare B: ", end='')
  #Taking the index value and printing it to the terminal
  for key, value in enumerate(compB):
    if key == 0:
      print(f"{compB[value]}, ", end='')
    elif key == 2:
      print(f"a {compB[value]}, ", end='')
    elif key == 1:
      coin2 = compB[value]
    elif key == 3:
      print(f"from {compB[value]}.")
  print("Who has more followers? 'A' or 'B'? ")
  choice = input().upper()
  if choice == 'A':
    if coin1 > coin2:
      user_score()
      clear()
      print(f"The current score is {score}")
      compare()
    else:
      clear()
      print(f"You lost, Final score is {score}")
  elif choice == 'B':
    if coin1 < coin2:
      user_score()
      clear()
      print(f"The current score is {score}")
      compare()
    else:
      clear()
      print(f"You lost, Final score is {score}")
  else:
    print("Invalid Character")

compare()