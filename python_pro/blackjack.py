import os
import platform
import random

def clear():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')


cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_cards = []
computer_cards = []
Is_game_over = False
def calculate_score(user_cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(user_cards)
def deal_cards():
    for _ in range(2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
    print(f"Computer First Hand is: {computer_cards[0]}")
    print(f"Your Cards are: {user_cards} and score is {user_score}")

def compare():
    while not Is_game_over:
        i = input("Want to hit, then click 'y', Want to Stand, then click 'n'").upper()
        if user_score == 0 or computer_score == 0 or user_score > 21:\
            Is_game_over = True

deal_cards()