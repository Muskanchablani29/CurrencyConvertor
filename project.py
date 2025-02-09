users = {}  # Dictionary to store username-password pairs

def signup():
    """Function to register a new user"""
    print("\nSign Up:")
    username = input("Enter a new username: ")
    if username in users:
        print("Username already exists! Try logging in.")
        return False
    password = input("Enter a password: ")
    users[username] = password
    print("Signup successful! You can now log in.")
    return True

def login():
    """Function to log in an existing user"""
    print("\nLogin:")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print(f"Welcome, {username}!")
        return True
    else:
        print("Invalid username or password! Please try again.")
        return False

def display_menu():
    """Displays the menu options"""
    print("\nCurrency Converter Menu:")
    print("1. Convert Currency")
    print("2. Update Exchange Rates")
    print("3. Logout")
    return input("Choose an option (1/2/3): ")

def currency_converter(amount, from_currency, to_currency, exchange_rates):
    """Converts currency based on hardcoded exchange rates"""
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return "Invalid currency code"

    amount_in_usd = amount / exchange_rates[from_currency]
    converted_amount = amount_in_usd * exchange_rates[to_currency]
    return round(converted_amount, 2)

def update_exchange_rates(exchange_rates):
    """Allows users to update exchange rates manually"""
    print("\nUpdate Exchange Rates:")
    for currency, rate in exchange_rates.items():
        new_rate = input(f"Enter new rate for {currency} (current: {rate}) or press Enter to keep unchanged: ")
        if new_rate.strip():
            try:
                exchange_rates[currency] = float(new_rate)
            except ValueError:
                print(f"Invalid input for {currency}, keeping old rate.")
    print("Exchange rates updated successfully!")

# Hardcoded exchange rates (relative to 1 USD)
exchange_rates = {
    "USD": 1.0, "EUR": 0.92, "GBP": 0.79, "INR": 83.0, "JPY": 148.6,
    "AUD": 1.54, "CAD": 1.35, "CNY": 7.19
}

while True:
    print("\nWelcome to the Currency Converter!")
    print("1. Sign Up")
    print("2. Login")
    print("3. Exit")
    main_choice = input("Choose an option (1/2/3): ")

    if main_choice == "1":
        signup()
    elif main_choice == "2":
        if login():  # Only proceed if login is successful
            while True:
                choice = display_menu()
                if choice == "1":  # Convert Currency
                    try:
                        amount = float(input("\nEnter amount: "))
                        from_currency = input("Enter from currency (e.g., USD, EUR): ").upper()
                        to_currency = input("Enter to currency (e.g., INR, GBP): ").upper()
                        result = currency_converter(amount, from_currency, to_currency, exchange_rates)
                        print(f"{amount} {from_currency} is approximately {result} {to_currency}")
                    except ValueError:
                        print("Invalid amount. Please enter a number.")
                elif choice == "2":  # Update Exchange Rates
                    update_exchange_rates(exchange_rates)
                elif choice == "3":  # Logout
                    print("Logging out...")
                    break
                else:
                    print("Invalid choice. Please enter 1, 2, or 3.")
    elif main_choice == "3":
        print("Thank you for using the currency converter. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
