import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "win"
    else:
        return "lose"

def print_choices(user_choice, computer_choice):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

def print_result(result):
    if result == "win":
        print("Congratulations you win!")
    elif result == "lose":
        print("Sorry you lose.")
    else:
        print("It's a DRAW")

def main():
    user_score = 0
    computer_score = 0
    
    while True:
        print("\nRock, Paper, Scissors Game")
        print("Choose: rock, paper, or scissors")
        
        user_choice = input("Your choice: ").strip().lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        
        print_choices(user_choice, computer_choice)
        print_result(result)
        
        if result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1
        
        print(f"\nScore - You: {user_score} | Computer: {computer_score}")
        
        play_again = input("\nDo you want to play again? |yes|no|: ").strip().lower()
        if play_again != 'yes':
            print("GIVE YOUR BEST")
            break

if __name__ == "__main__":
    main()
