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
    print("\nAvailable Games:")

    for game, details in game_library.items():
        if details["quantity"] > 0:
            print(f"{game}: {details['quantity']} available, Cost: ${details['cost']} per game")
        
    input("Press enter to go back")


# Function to register a new user
def register_user():
    while True:
        try:
            print("\nREGISTRATION PAGE")

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
    print("\nRENT A GAME")

    print("Available Games:")
    available_games = []

    for game, details in game_library.items():
        if details["quantity"] > 0:
            available_games.append(game)
            print(f"{game}: {details['quantity']} copy(s) available, Cost ${details['cost']} per copy")

    if not available_games:
        print("No games available for rent at the moment.")
        input("Press enter to go back")
        return

    selected_game = input("Enter the name of the game you want to rent: ")

    if selected_game in available_games:
        game_details = game_library[selected_game]
        cost = game_details["cost"]

        if game_details["quantity"] > 0:
            if user_accounts[username]["Balance"] >= cost:
                user_accounts[username]["Balance"] -= cost
                game_library[selected_game]["quantity"] -= 1
                user_accounts[username]["rented_games"].append(selected_game)
                print(f"You have successfully rented '{selected_game}'. Enjoy!")
            else:
                print("Insufficient balance to rent the game.")
        else:
            print("Sorry, no copies of this game are currently available.")
    else:
        print("Invalid game selection.")

    input("Press enter to go back")




# Function to return a game
def return_game(username):
    print("\nRETURN A GAME")

    # Check if user has any rented games
    if not user_accounts[username]["rented_games"]:
        print("You have no games rented.")
        input("Press enter to go back")
        return

    # Display games currently rented by the user
    print("Games currently rented:")
    for idx, game in enumerate(user_accounts[username]["rented_games"], start=1):
        print(f"{idx}. {game}")

    try:
        choice = int(input("Enter the number of the game you want to return (or 0 to cancel): "))

        if choice == 0:
            print("Returning to main menu.")
            return

        if 1 <= choice <= len(user_accounts[username]["rented_games"]):
            game_to_return = user_accounts[username]["rented_games"][choice - 1]

            game_library[game_to_return]["quantity"] += 1

            user_accounts[username]["rented_games"].remove(game_to_return)

            print(f"'{game_to_return}' has been returned successfully.")
        else:
            print("Invalid choice. Please select a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

    input("Press enter to go back")



# Function to top-up user account
def top_up_account(username, amount):
    print("\nTOP-UP ACCOUNT")

    try:
        amount = float(amount)
        if amount > 0:
            if username in user_accounts:
                user_accounts[username]["Balance"] += amount

                # Calculate points earned based on top-up amount ($2 spent = 1 point)
                points_earned = int(amount / 2)
                user_accounts[username]["Points"] += points_earned

                print(f"Account topped up successfully. Current balance: ${user_accounts[username]['Balance']}")
                print(f"You earned {points_earned} points with this top-up.")
            else:
                print("User not found.")
        else:
            print("Invalid amount entered.")
    except ValueError:
        print("Please enter a valid amount.")

    input("Press enter to go back")



# Function to display user's inventory
def display_inventory(username):
    print("\nYOUR RENTED GAMES")

    if user_accounts[username]["rented_games"]:
        for game in user_accounts[username]["rented_games"]:
            print(f"- {game}")
    else:
        print("You currently have no games rented.")

    input("Press enter to go back")


# Function for admin to update game details
def admin_update_game():
    print("\nUPDATE GAME DETAILS")

    print("Available Games:")
    for game, details in game_library.items():
        print(f"{game}: Quantity - {details['quantity']}, Cost - ${details['cost']}")

    try:
        game_to_update = input("Enter the name of the game you want to update: ")

        if game_to_update in game_library:
            new_quantity = int(input("Enter the new quantity of the game: "))
            new_cost = float(input("Enter the new rental cost of the game: "))

            game_library[game_to_update]["quantity"] = new_quantity
            game_library[game_to_update]["cost"] = new_cost

            print(f"'{game_to_update}' details updated successfully.")
        else:
            print("Game not found.")
    except ValueError:
        print("Invalid input. Please enter a valid quantity and cost.")

    input("Press enter to go back")


# Function for admin login
def admin_login():
    print("\nADMIN LOGIN PAGE")

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
            print("\nADMIN MENU")
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
    print("\nREDEEM FREE GAME RENTAL")

    points_earned = user_accounts[username]["Balance"] // 2

    if points_earned >= 3:  
        free_game_count = points_earned // 3
        remaining_points = points_earned % 3

        if free_game_count > 0:
            user_accounts[username]["Points"] += remaining_points  
            user_accounts[username]["Balance"] -= (free_game_count * 3 * 2)  # Deduct balance for redeemed games

            print(f"Congratulations! You have redeemed {free_game_count} free game(s).")
        else:
            print("You do not have enough points to redeem a free game.")
    else:
        print("You do not have enough points to redeem a free game.")

    input("Press enter to go back")


# Function to display game inventory
def display_game_inventory():
    print("\nGAME INVENTORY")

    for game, details in game_library.items():
        print(f"{game}: {details['quantity']} available")

    input("Press enter to go back")


# Function to handle user's logged-in menu
def logged_in_menu(username):
    while True:
        try:
            print(f"\nWELCOME {username}!")
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
                amount = input("Enter the amount to top up: ")
                top_up_account(username, amount)
            elif choice == "4":
                display_inventory(username)
            elif choice == "5":
                redeem_free_rental(username)
            elif choice == "6":
                print("Logging out.")
                return
            else:
                print("Please input a valid option")

        except ValueError:
            print("Please enter a correct input.")


# Function to check user credentials
def check_credentials():
    print("\nLOGIN PAGE")

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
                print("\nWELCOME TO RENTAL GAME SYSTEM")
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