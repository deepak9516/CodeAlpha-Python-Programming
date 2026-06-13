import csv
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 130
}

portfolio = {}
total_investment = 0

print("Stock Portfolio Tracker")
print("Available Stocks:", stock_prices.keys())

def check_stocks(user_stock_name):
    if user_stock_name in stock_prices:
        return True
    else:
        print("No, stock is not available.")
        return False

while True:
    
    user_stock_name = input("Which stock you want to buy: ").upper()
    
    if not check_stocks(user_stock_name):
        continue
    
    user_stock_quantity = int(input("How many shares: "))
    
    price = stock_prices[user_stock_name]
    cost = price * user_stock_quantity
    
    portfolio[user_stock_name] = portfolio.get(user_stock_name,0) +user_stock_quantity
    total_investment += cost
    
    print(f"Added {user_stock_quantity} {user_stock_name} shares worth ${cost}")

    ask_user = input("Do you want to buy more stocks? (yes/no): ").lower()
    
    if ask_user != "yes":
        break
with open("my_portfolio.csv","w",newline="",encoding= "utf-8")as file:
    writer = csv.DictWriter(file,fieldnames = ["stock","quantity"])
    writer.writeheader()
    for stock, qty in portfolio.items():
        writer.writerow({
            "stock": stock,
            "quantity" : qty
        })
    
    
print("\nFinal Portfolio ")

for stock, qty in portfolio.items():
    print(f"{stock} : {qty} shares")
    
    
print(f"Total investment: ${total_investment}")



