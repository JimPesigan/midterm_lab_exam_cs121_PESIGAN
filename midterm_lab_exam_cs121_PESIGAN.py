# Dictionary to store game library with their quantities and rental costs
game_library = {
    "Donkey Kong": {"quantity": 3, "cost": 2},
    "Super Mario Bros": {"quantity": 5, "cost": 3},
    "Tetris": {"quantity": 2, "cost": 1},
    # Add more games as needed
}


# Dictionary to store user accounts with their balances and points
user_accounts = {}


# Function to display available games with their numbers and rental costs
def display_available_games():
    print("Available Games:")

    for game, details in game_library.items():
        if details["quantity"] > 0:
            print(f"{game}: {details['quantity']} available, Cost: ${details['cost']} per game")
        
    input("Press enter to go back")


# Function to register a new user
def register_user():
    while True:
        try:
            print("REGISTRATION PAGE")

            username = input("Please enter your username:")
            password= input("Please enter your passwrd:")

            if username in user_accounts:
                print("Username already exists. Please enter another one.")
            else:
                print("Account registered successfully.")
                user_accounts[username] = {
                "username": username,
                "password": password,
                "Balance": 0,
                "Points": 0,
                "rented_games": []
                }
                return
        except ValueError:
            print("Please enter a correct imput.")        
    

# Function to rent a game
def rent_game(username):
    pass


# Function to return a game
def return_game(username):
    pass


# Function to top-up user account
def top_up_account(username, amount):
    pass


# Function to display user's inventory
def display_inventory(username):
    pass


# Function for admin to update game details
def admin_update_game(username):
    pass


# Function for admin login
def admin_login():
    print("ADMIN LOGIN PAGE")

    admin_username = input("Username: ")
    admin_password = input("Password: ")

    if admin_username == "admin" and admin_password == "adminpass":
        print("Login Successful!")
        admin_menu()
    else:
        print("Invalid username or password.")


# Admin menu
def admin_menu():
    while True:
        try:
            print("Admin Menu")
            print("1. Update Game Details")
            print("2. Log out")

            choice = input("Enter your choice: ")

            if choice == "1":
                admin_update_game()
            elif choice == "2":
                print("Logging out.")
                return
            else:
                print("Please input a valid option")
        except ValueError:
            print("Please enter a correct input.")      
            return

# Function for users to redeem points for a free game rental
def redeem_free_rental(username):
    pass


# Function to display game inventory
def display_game_inventory():
    pass


# Function to handle user's logged-in menu
def logged_in_menu(username):
    while True:
        try:
            print(f"Welcome {username}!")
            print("1. Rent a game")
            print("2. Return a game")
            print("3. Top-up Account")
            print("4. Display inventory")
            print("5. Redeem free game rental")
            print("6. Log out")

            choice = input("Please enter your choice: ")

            if choice == "1":
                rent_game(username)
            elif choice == "2":
                return_game(username)
            elif choice == "3":
                top_up_account(username, amount)
            elif choice == "4":
                display_game_inventory()
            elif choice == "5":
                redeem_free_rental(username)
            elif choice == "6":
                print("Logging out.")
                return


            else:
                print("Please input a valid option")

        except ValueError:
            print("Please enter a correct input.")      
            return


# Function to check user credentials
def check_credentials():
    print("LOGIN PAGE")

    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    if username in user_accounts and user_accounts[username]["password"] == password:
        print("Login Successful.")
        logged_in_menu(username)
    else:
        print("Invalid username or password.")
        
    
# Main function to run the program
def main():
    while True:
        try:
                print("WELCOME TO RENTAL GAME SYSTEM")
                print("1. Display Available Games")
                print("2. Register User")
                print("3. Login")
                print("4. Admin Login")
                print("5. Exit ")

                choice = input("Please enter your choice: ")

                if choice == "1":
                    display_available_games()
                elif choice =="2":
                    register_user()
                elif choice =="3":
                    check_credentials()
                elif choice =="4":
                    admin_login()
                elif choice =="5":
                    print("Thank you for using the system, Goodbye!")
                    return
                else:
                    print("Invalid Choice! Please enter a valid option")           
        except ValueError:
            print("Please enter a correct input.")      
            return  


main()