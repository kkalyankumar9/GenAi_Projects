import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").strip().lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'draw'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def update_score(winner, scores):
    scores[winner] += 1
    return scores

def display_score(scores):
    print(f"User wins: {scores['user']}")
    print(f"Computer wins: {scores['computer']}")
    print(f"Draws: {scores['draw']}")

def play_again():
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    return play_again == 'yes'

def main():
    scores = {'user': 0, 'computer': 0, 'draw': 0}
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chooses: {computer_choice}")
        winner = determine_winner(user_choice, computer_choice)
        print(f"Result: {winner.capitalize()} wins!\n")
        scores = update_score(winner, scores)
        display_score(scores)
        if not play_again():
            break

    print("Thank you for playing Rock, Paper, Scissors!")

if __name__ == "__main__":
    main()
