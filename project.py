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
    "RUB": 75.0, "DKK": 6.66, "PKR": 166.0, "ILS": 3.41, "PLN": 3.97,
    "COP": 3590.0, "CLP": 710.0, "ARS": 710.0, "VND": 22400.0, "TWD": 30.0,
    "UAH": 27.0, "RON": 4.0, "CZK": 21.0, "BGN": 1.0, "HRK": 7.0,
    "BHD": 0.37, "JOD": 0.71, "OMR": 0.39, "QAR": 3.64, "SYP": 2.5,
    "LBP": 1507.5, "JMD": 141.0, "TTD": 6.75, "TZS": 2315.0, "UGX": 3750.0,
    "GHS": 5.8, "MAD": 9.5, "BSD": 1.0, "FJD": 2.15, "NPR": 119.0,
    "LKR": 185.0, "PKR": 166.0, "SCR": 13.75, "MUR": 40.0, "BBD": 2.0,
    "BZD": 2.0, "BMD": 1.0, "GYD": 209.0, "HTG": 100.0, "HNL": 24.0,
    "JOD": 0.71, "KZT": 418.0, "LAK": 9000.0, "LKR": 185.0, "LRD": 200.0,
    "MNT": 2850.0, "MVR": 15.5, "NAD": 17.0, "NGN": 360.0, "NIO": 34.0,
    "NPR": 119.0, "PAB": 1.0, "PGK": 3.4, "PYG": 6500.0, "RWF": 950.0,
    "SBD": 8.0, "SLL": 9800.0, "SOS": 580.0, "SRD": 7.5, "STD": 21000.0,
    "SZL": 17.0, "TOP": 2.3, "TTD": 6.75, "TVD": 1.3, "VUV": 112.0,
    "WST": 2.6, "XAF": 600.0, "XCD": 2.7, "XOF": 600.0, "XPF": 100.0,
    "YER": 250.0, "ZMW": 18.0, "ZWL": 322.0,
    "AFN": 71.0, "BDT": 84.0, "BIF": 2000.0, "CVE": 100.0, "DJF": 177.0,
    "GNF": 8600.0, "IRR": 42000.0, "KMF": 450.0, "MGA": 4000.0, "MRU": 35.0,
    "RSD": 100.0, "RWF": 1000.0, "XAF": 600.0, "XOF": 600.0, "XPF": 100.0,
    "ZAR": 17.0, "ZMK": 9000.0, "ZWL": 322.0
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
