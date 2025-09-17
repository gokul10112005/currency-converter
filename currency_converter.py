# Currency Converter - Offline Version

# Fixed exchange rates (base: USD)
rates = {
    "USD": 1,        # Base Currency
    "INR": 83.2,
    "EUR": 0.92,
    "GBP": 0.79,
    "JPY": 147.5
}


def convert(amount, from_currency, to_currency):
    if from_currency not in rates or to_currency not in rates:
        return "Currency not supported"

    # Convert to USD first, then to target currency
    amount_in_usd = amount / rates[from_currency]
    converted = amount_in_usd * rates[to_currency]
    return round(converted, 2)


# Main Program
print("💱 Currency Converter (Offline Version) 💱")
print("Supported currencies:", ", ".join(rates.keys()))

while True:
    try:
        amount = float(input("Enter amount: "))
        from_curr = input("From Currency: ").upper()
        to_curr = input("To Currency: ").upper()

        result = convert(amount, from_curr, to_curr)
        print(f"{amount} {from_curr} = {result} {to_curr}")

    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")

    cont = input("Do you want to convert again? (yes/no): ").lower()
    if cont != "yes":
        print("👋 Thank you for using Currency Converter!")
        break
