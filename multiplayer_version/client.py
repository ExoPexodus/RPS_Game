import socket

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower().strip()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Try again.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower().strip()
    return user_choice

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 5555))

    welcome_msg = client_socket.recv(1024).decode()
    print(welcome_msg)

    player_number = client_socket.recv(1024).decode()
    print(player_number)

    while True:
        print(client_socket.recv(1024).decode())
        user_choice = get_user_choice()
        client_socket.send(user_choice.encode())
        if user_choice != "":
            print(client_socket.recv(1024).decode())
            other_choice = client_socket.recv(1024).decode()
            if other_choice != "":
                print(other_choice)
                break

    client_socket.close()

if __name__ == "__main__":
    start_client()
