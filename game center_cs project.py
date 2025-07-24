import csv
import random

file_name = "users.csv"  

def save_user(username, password):
    
    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

def is_username_taken(username):
    
    try:
        with open(file_name, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == username:
                    return True
    except FileNotFoundError:
        return False  
    return False

def verify_user(username, password):
    
    try:
        with open(file_name, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == username and row[1] == password:
                    return True
    except FileNotFoundError:
        return False 
    return False

def register():
    
    print("\n=== Register ===")
    username = input("Choose a username: ").strip()
    
    if is_username_taken(username):
        print("That username is already taken. Try again.")
        return register()

    password = input("Choose a password: ").strip()
    save_user(username, password)
    print("Registration successful! You can now log in.")
    return username

def login():
    
    print("\n=== Login ===")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    if verify_user(username, password):
        print("Login successful! Welcome," + username +".")
        return username
    else:
        print("Incorrect username or password.")
        choice = input("Forgot your password? (yes/no): ").strip().lower()
        if choice == "yes":
            return reset(username)
        else:
            print("Try logging in again.")
            return login()

def reset(username):
    
    print("\n=== Reset Password ===")
    new_password = input("Enter a new password: ").strip()

    users = []
    try:
        with open(file_name, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == username:
                    users.append([username, new_password])  
                else:
                    users.append(row)
    except FileNotFoundError:
        print("No user data found. Please register first.")
        return register()

    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(users)

    print("Password reset successful! You can now log in.")
    return username

def main():
    
    print("--------------------")

    while True:
        choice = input("\nDo you have an account? (yes/no/exit): ").strip().lower()

        if choice == "yes":
            username = login()
            break
        elif choice == "no":
            username = register()
            break
        elif choice == "exit":
            print("Goodbye!")
            return
        else:
            print("Invalid input. Please type 'yes', 'no', or 'exit'.")

    print("\nWe currently have two games to choose from:")
    print("1. Rock, Paper, Scissors")
    print("2. Encryptor/Decryptor")

    while True:
        game_choice = input("Please enter which game you want to play (1/2): ").strip()

        if game_choice == "1":
            rps(username)  
            break
        elif game_choice == "2":
            ed(username)  
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
            return


#ROCK PAPER SCISSOR
def rps(username):
    print("Let's begin Rock, Paper, Scissors!")
    game_choices = ["rock", "paper", "scissors"]
    
    while True:
        player = input("Enter your choice (rock, paper, or scissors): ").lower()
        if player not in game_choices:
            print("Please cooperate.")
            continue

        computer = random.choice(game_choices)
        print("You chose: " + player + ", Computer chose: " + computer)
        
        result = determine_winner(player, computer)
        print(result)

        with open("GAME_CENTER!.csv", "a") as file:
            file.write("\n" + username + " chose: " + player + ", Computer chose: " + computer + " Result: " + result)

        play_again = input("Would you like to play again? (y/n): ").lower()
        if play_again != 'y':
            
            sq1 = input("Would you like to try our encryptor decryptor game then? Press 1 to continue and 2 to exit (1/2): ")
            if sq1 == '1':
                ed(username)
                break  
            else:
                print('Alright! Have a good day!')
                return  



def determine_winner(player, computer):
    """Determines the winner of the game."""
    if player == computer:
        return "It's a draw!"
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        return "You win!"

    else:
        return "You lose!"

#ENCRYPTOR DECRYPTOR    

def ed(username):
    print("You have chosen to use our encryptor and decryptor.")

    while True:
        op = input("Press 1 to encrypt text and 2 to decrypt text: ").strip()
        if op not in ['1', '2']:
            print("Invalid choice. Please enter 1 or 2.")
            continue

        if op == '1':
            text = input("Enter the text to encrypt: ")
            encrypted = ''.join([chr(ord(c) - 5) if c != " " else " " for c in text])
            print("Encrypted text: " + encrypted)
            with open("GAME_CENTER!.csv", "a") as file:
                file.write("\n" + username + " encrypted text: " + encrypted)
        
        elif op == '2':
            encrypted_text = input("Enter encrypted text: ")
            decrypted = ''.join([chr(ord(c) + 5) if c != " " else " " for c in encrypted_text])
            print("Decrypted text: " + decrypted)
            with open("GAME_CENTER!.csv", "a") as file:
                file.write("\n" + username + " decrypted text: " + decrypted)
        
        play_again = input("Would you like to try again? (y/n): ").lower()
        if play_again != 'y':
            sq1 = input("Would you like to try our rock paper scissors game then? Press 1 to continue and 2 to exit (1/2): ")
            if sq1 == '1':
                rps(username)
                return  
            else:
                print("Have a good day!")
                return  
                




if __name__ == "__main__":
    print(".................................................................GAME CENTER......................................................................")
    start = input("Welcome!Want to run game? (yes/no): ").strip().lower()
    if start == "yes":
        main()
         
    elif start == "no":
        print("Bye!")
        
    else:
        print('Invalid input')
