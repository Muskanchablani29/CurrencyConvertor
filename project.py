import time
import os

users = {}

def print_slowly(text, delay=0.001):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def print_slowly2(text2, delay=0.1):
    for char in text2:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def signup():
    print("\nSign Up:")
    username = input("Enter a new username: ")
    if username in users:
        print("Username already exists! Try logging in.")
        return False
    password = input("Enter a password: ")
    users[username] = password
    print("Signup successful! You can now log in.")
    time.sleep(1)
    os.system('cls')
    return True

def login():
    print("\nLogin:")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print(f"Welcome, {username}!")
        time.sleep(1)
        os.system('cls')
        return True
    else:
        print("Invalid username or password! Please try again.")
        return False

def display_menu():
    print_slowly("="*80)
    print_slowly2("\t\t\t\t\tCurrency Converter Menu:")
    print_slowly("="*80)
    print("\t\t\t\t\t1. Convert Currency")
    print("\t\t\t\t\t2. Update Exchange Rates")
    print("\t\t\t\t\t3. Logout")
    return input("Choose an option (1/2/3): ")

def currency_converter(amount, from_currency, to_currency, exchange_rates):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return "Invalid currency code"

    amount_in_usd = amount / exchange_rates[from_currency]
    converted_amount = amount_in_usd * exchange_rates[to_currency]
    return round(converted_amount, 2)

def update_exchange_rate(exchange_rates):

    print("\nUpdate a Single Exchange Rate:")
    currency = input("Enter the currency code you want to update (e.g., USD, EUR): ").upper()
    if currency in exchange_rates:
        new_rate = input(f"Enter new rate for {currency} (current: {exchange_rates[currency]}): ")
        try:
            exchange_rates[currency] = float(new_rate)
            print(f"Exchange rate for {currency} updated successfully!")
        except ValueError:
            print(f"Invalid input for {currency}, keeping old rate.")
    else:
        print("Invalid currency code.")

exchange_rates = {
    "USD": 1.0, "EUR": 0.92, "GBP": 0.79, "INR": 83.0, "JPY": 148.6,
    "AUD": 1.54, "CAD": 1.35, "CNY": 7.19 , "SGD": 1.43, "CHF": 0.98 ,
    "MYR": 4.34, "NZD": 1.66, "THB": 31.22, "HUF": 306.0, "AED": 3.67,
    "HKD": 7.75, "MXN": 22.0, "ZAR": 17.0, "PHP": 50.51, "SEK": 9.58,
    "IDR": 14125.0, "SAR": 3.75, "BRL": 5.29, "TRY": 6.85, "KES": 106.0,
    "KRW": 1195.0, "EGP": 15.7, "IQD": 1190.0, "NOK": 10.35, "KWD": 0.30,
    "RUB": 75.0, "DKK": 6.66, "PKR": 166.0, "ILS": 3.41, "PLN": 3.97
}

while True:
    print_slowly("="*80)
    print_slowly2("\t\t\t\tWelcome to the Currency Converter!")
    print_slowly("="*80)
    print("\t\t\t\t\t1. Sign Up")
    print("\t\t\t\t\t2. Login")
    print("\t\t\t\t\t3. Exit")
    main_choice = input("Choose an option (1/2/3): ")

    if main_choice == "1":
        signup()
    elif main_choice == "2":
        if login():  
            while True:
                choice = display_menu()
                if choice == "1":  
                    try:
                        amount = float(input("\nEnter amount: "))
                        from_currency = input("Enter from currency (e.g., USD, EUR): ").upper()
                        to_currency = input("Enter to currency (e.g., INR, GBP): ").upper()
                        result = currency_converter(amount, from_currency, to_currency, exchange_rates)
                        print(f"{amount} {from_currency} is approximately {result} {to_currency}")
                    except ValueError:
                        print("Invalid amount. Please enter a number.")
                elif choice == "2":  
                    update_exchange_rate(exchange_rates)
                elif choice == "3": 
                    print("Logging out...")
                    break
                else:
                    print("Invalid choice. Please enter 1, 2, or 3.")
    elif main_choice == "3":
        print("Thank you for using the currency converter. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
