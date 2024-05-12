import random
import time

invalid_choice_responses = [
    "Oh come on! You can do better than this... Fix your spellings!",
    "Seriously? You're better than that! Try again.",
    "Invalid choice! Let's try this again.",
    "Hmm... Are you sure you know how to spell? Try once more."
]

tie_responses = [
    "Really!? Wow, you guys ended up in a tie... Congrats, I guess?",
    "It's a tie! The battle continues...",
    "A tie! Looks like neither of you wants to give up."
]

win_responses = [
    "Good job, you won... for once.",
    "You're on fire! You beat the computer!",
    "Congratulations! You've emerged victorious this time."
]

lose_responses = [
    "Damn, even the computer can beat you? That's crazy...",
    "Better luck next time! The computer outsmarted you.",
    "You'll get 'em next time! Don't give up!"
]

def get_user_choice():
    user_choice = input("Rock, paper, or scissors? ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print(random.choice(invalid_choice_responses))
        user_choice = input("Rock, paper, or scissors? ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return random.choice(tie_responses)
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return random.choice(win_responses)
    else:
        return random.choice(lose_responses)

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