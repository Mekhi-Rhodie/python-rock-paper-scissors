game_active = True
user_wins = 0
user_score = 0
cpu_wins = 0
cpu_score = 0
cpu_choices = ['Rock', 'Paper', 'Scissors']


def game(user_score, cpu_score):
    user_choice = input("Rock, Paper, or Scissors?:  ").title()
    cpu_choice = set(cpu_choices).pop()

    if user_choice == "Rock" and cpu_choice == 'Paper':
        cpu_score += 1
        print(f"CPU Wins! :({cpu_score}")
    elif (user_choice == "Rock" and cpu_choice == 'Scissors'):
        user_score += 1
        print(f"User Wins! {user_score}")
    else:
        print("This round is a tie!")

    if user_choice == "Paper" and cpu_choice == "Scissors":
        cpu_score += 1
        print(f"CPU Wins! :({cpu_score}")
    elif user_score == "Scissors" and cpu_choice == "Paper":
        user_score += 1
        print(f"User Wins! {user_score}")
    else:
        print("This round is a tie!")

    if user_score == 3:
        print("User Has Won the Game!!")
        user_wins += 1
        game_active = False
    elif cpu_score == 3:
        print("CPU Has Won the Game! X(")
        cpu_wins += 1
        game_active = False


game(user_score, cpu_score)
