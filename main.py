import random

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2

def print_roll(dice1, dice2):
    print(f"The sum of dice is {dice1} + {dice2} = {dice1+dice2}")

def play_game():
    while True:
        dice1, dice2 = roll_dice()
        print_roll(dice1, dice2)
        total = dice1 + dice2

        if total in [7, 11]:
            print("You win!")
            break
        elif total in [2, 3, 12]:
            print("You lose.")
            break
        else:
            print(f"The sum of dice is {dice1} + {dice2} = {dice1+dice2}. Now, your goal is {total}. Roll again.")
            goal = total
            while True:
                dice1, dice2 = roll_dice()
                print_roll(dice1, dice2)
                total = dice1 + dice2
                if total == goal:
                    print("You win!")
                    return
                elif total == 7:
                    print("You lose.")
                    return

play_game()