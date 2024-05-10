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
    pass

# Function to register a new user
def register_user():
    print("REGISTRATION PAGE")

    username = input("Please enter your username:")
    password = input("Please enter your passwrd:")

    if username in user_accounts:
        print()

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
    admin_username = "admin"
    admin_password = "adminpass"

    pass

# Admin menu
def admin_menu():
    pass

# Function for users to redeem points for a free game rental
def redeem_free_rental(username):
    pass

# Function to display game inventory
def display_game_inventory():
    pass

# Function to handle user's logged-in menu
def logged_in_menu(username):
    pass

# Function to check user credentials
def check_credentials(username, password):
    pass
    
# Main function to run the program
def main():
    while True:
        try:
                print("WELCOME TO RENTAL GAME SYSTEM")
                print("1. Display Available Games")
                print("1. Register Usser")
                print("1. Login")
                print("1. Admin Login")
                print("1. Exit ")

                choice = input("Please enter your choice:")

                if choice == "1":
                    display_available_games()
                elif choice =="2":
                    register_user()
                elif choice =="3":
                    check_credentials(username, password)
                elif choice =="4":
                    admin_login()
                elif choice =="5":
                    print("Thank you for using the system, Goodbye!")
                    return
                else:
                    print("Invalid Choice! Please enter a valid option")           
        except ValueError:
            print("Please enter a correct imput")      
            return  


if _name_ == "_main_":
    main()