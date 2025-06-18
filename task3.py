class StockPortfolio:
    def __init__(self):
        self.stock_prices = {
            "AAPL": 180,
            "TSLA": 250,
            "GOOG": 140,
            "AMZN": 130
        }
    def get_stock_input(self):
        stock = input("Enter stock symbol (AAPL, TSLA, GOOG, AMZN): ").strip().upper()
        if stock not in self.stock_prices:
            raise ValueError("Stock not found.")
        return stock
    def get_quantity_input(self):
        try:
            quantity = int(input("Enter number of shares: "))
            if quantity < 0:
                raise ValueError("Quantity cannot be negative.")
            return quantity
        except ValueError:
            raise ValueError("Invalid quantity. Must be a positive integer.")
    def calculate_total(self, stock, quantity):
        return self.stock_prices[stock] * quantity
    def save_to_file(self, stock, total):
        result = f"Total investment in {stock}: ${total}"
        try:
            with open("investment.txt", "w") as f:
                f.write(result)
            print(result)
            print(" Investment details saved to 'investment.txt'.")
        except IOError:
            print(" Failed to save the file.")
    def run(self):
        print("Welcome to the Stock Portfolio Tracker")
        try:
            stock = self.get_stock_input()
            quantity = self.get_quantity_input()
            total = self.calculate_total(stock, quantity)
            self.save_to_file(stock, total)
        except ValueError as ve:
            print(f" Error: {ve}")
portfolio = StockPortfolio()
portfolio.run()
