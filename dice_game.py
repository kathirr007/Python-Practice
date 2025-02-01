import random

def roll_dice():
    dice_rolled = random.randint(1,6) + random.randint(1,6)
    return dice_rolled

def main():

    player1 = input('Enter player1 name: \n')
    player2 = input('Enter player2 name: \n')

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(f"{player1} rolled {roll1}")
    print(f"{player2} rolled {roll2}")

    if roll1 > roll2:
        print(f"Player {player1} won..!")
    elif roll2 > roll1:
        print(f"Player {player2} won..!")
    
    else:
        print("Sorry, it's a tie")
        

main()