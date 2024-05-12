import random
import time

def get_user_choice():
    user_choice = input("Rock, paper, or scissors? ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("oh come on! you can do better than this.. fix your spellings!")
        user_choice = input("Rock, paper, or scissors? ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "really!? wow, you guys ended up in a tie... congrats ig?"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "good job, you won... for once."
    else:
        return "Damn, even the computer can beat you? that's crazy..."

def animate_hand(choice):
    if choice == 'rock':
        print("   _______")
        print("---'   ____)")
        print("      (_____)")
        print("      (_____)")
        print("      (____)")
        print("---.__(___)")
    elif choice == 'paper':
        print("    _______")
        print("---'    ____)____")
        print("           ______)")
        print("          _______")
        print("         _______)")
        print("---.__________)")
    elif choice == 'scissors':
        print("    _______")
        print("---'    ____)____")
        print("           ______)")
        print("        __________)")
        print("       (____)")
        print("---.__(___)")
    time.sleep(1)

def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("\nYou chose:")
        animate_hand(user_choice)
        print("\nThe computer chose:")
        animate_hand(computer_choice)
        print("\n" + determine_winner(user_choice, computer_choice))
        play_again = input("\nDo you want to play again? (yes/no) ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

play_game()
