exchange_rate = 0.8665
usd_prices = [19.99, 49.50, 5.00, 120.00, 8.75, 250.99]

print("---> Product Price Conversion (USD to EUR) <---")
print(f"Using Exchange Rate: 1 USD = {exchange_rate} EUR\n")

for index, usd_price in enumerate(usd_prices, start=1):
    eur_price = usd_price * exchange_rate
    
    print(f"Product {index}: ${usd_price:.2f} USD  -->  €{eur_price:.2f} EUR")
