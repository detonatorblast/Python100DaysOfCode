# This code implements a simple Rock, Paper, Scissors game where the user plays against the computer.

import random


def play_game():
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        return play_game()
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    play_game()
    while input("Do you want to play again? (yes/no): ").lower() == "yes":
        play_game()
    print("Thanks for playing!")

