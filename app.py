from random import randint

game_active = True
user_wins = 0
user_score = 0
cpu_wins = 0
cpu_score = 0
cpu_choices = ['Rock', 'Paper', 'Scissors']


def game(user_score, cpu_score):
    user_choice = input("Rock, Paper, or Scissors?:  ").title()
    cpu_choice = cpu_choices[randint(0, 2)]
    print(f"You chose:  {user_choice}")
    print(f"The computer chose:  {cpu_choice}")

    if user_choice == 'Rock' and cpu_choice == 'Paper':
        cpu_score += 1
        print(f"CPU Wins! :(  {cpu_score}")
        return
    elif user_choice == 'Rock' and cpu_choice == 'Scissors':
        user_score += 1
        print(f"User Wins!  {user_score}")
        return
    elif user_choice == 'Paper' and cpu_choice == 'Rock':
        user_score += 1
        print(f"User Wins!  {user_score}")
        return
    elif user_choice == 'Paper' and cpu_choice == 'Scissors':
        cpu_score += 1
        print(f"CPU Wins! :(  {cpu_score}")
        return
    elif user_score == 'Scissors' and cpu_choice == 'Paper':
        user_score += 1
        print(f"User Wins! {user_score}")
        return
    elif user_choice == 'Scissors' and cpu_choice == 'Rock':
        cpu_score += 1
        print(f"CPU Wins! :(  {cpu_score}")
        return
    else:
        print("This round is a tie!")
        return


while game_active == True:
    game(user_score, cpu_score)
    if user_score == 3:
        print("You have Won the Game!")
        game_active = False
        break
    elif cpu_score == 3:
        print("The CPU has Won the Game! X(")
        game_active = False
        break
