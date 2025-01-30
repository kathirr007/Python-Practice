computer_choice = 'scissors'
user_choice = input('Do you want rock, paper or scissors?\n')
user_won = "Great you won..!"

if computer_choice == user_choice:
    print("It's a TIE")
elif user_choice == 'rock' and computer_choice == 'scissors':
    print(user_won)
elif user_choice == 'scissors' and computer_choice == 'paper':
    print(user_won)
elif user_choice == 'paper' and computer_choice == 'rock':
    print(user_won)
else:
    print("Oh, You Loose, Computer WON :(")