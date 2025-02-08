import requests
from decimal import Decimal

def get_exchange_rates(base_currency):
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
        response = requests.get(url, timeout=10)  # Added timeout
        response.raise_for_status()  # Raises exception for bad status codes
        return response.json()["rates"]
    except requests.RequestException as e:
        print(f"Error fetching exchange rates: {e}")
        return None

def convert_currency(amount, from_currency, to_currency, rates):
    try:
        if not rates:
            return None
        if from_currency not in rates or to_currency not in rates:
            print(f"Invalid currency code. Please choose from: {', '.join(rates.keys())}")
            return None
        
        # Use Decimal for more precise calculations
        conversion_rate = Decimal(str(rates[to_currency])) / Decimal(str(rates[from_currency]))
        return round(Decimal(str(amount)) * conversion_rate, 2)
    except (ValueError, TypeError, ZeroDivisionError) as e:
        print(f"Error during conversion: {e}")
        return None

def main():
    base_currency = "USD"
    rates = get_exchange_rates(base_currency)
    if not rates:
        return
    
    while True:
        try:
            print("\nAvailable currencies:", ", ".join(sorted(rates.keys())))
            from_currency = input("Enter currency to convert from (or 'q' to quit): ").upper()
            
            if from_currency.lower() == 'q':
                break
                
            to_currency = input("Enter currency to convert to: ").upper()
            amount = float(input("Enter amount: "))
            
            if amount < 0:
                print("Please enter a positive amount")
                continue
                
            result = convert_currency(amount, from_currency, to_currency, rates)
            if result is not None:
                print(f"{amount:,.2f} {from_currency} = {result:,.2f} {to_currency}")
            
        except ValueError:
            print("Invalid input. Please enter a valid number for amount.")
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break

if __name__ == "__main__":
    main()
