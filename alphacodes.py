#hangman game
import random
words = ["apple", "chair", "robot", "clock", "train"]
word = random.choice(words)
hidden = "_" * len(word)
attempts = 6
while attempts > 0 and "_" in hidden:
    print("Word:", " ".join(hidden))
    guess = input("Guess a letter: ").lower()
    if guess in word:
        new_hidden = ""
        for i in range(len(word)):
            if word[i] == guess:
                new_hidden += guess
            else:
                new_hidden += hidden[i]
        hidden = new_hidden
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)
if "_" not in hidden:
    print("You won! The word was:", word)
else:
    print("You lost! The word was:", word)
#chatbot game
def chatbot():
    while True:
        user = input("You: ").lower()
        if user in ["hi", "hello"]:
            print("Bot: Hello!")
        elif user == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: I don't understand.")

chatbot()
#stocklist
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130
}
stock = input("Enter stock symbol (AAPL, TSLA, GOOG, AMZN): ").upper()
if stock in stock_prices:
    quantity = int(input("Enter number of shares: "))
    total = stock_prices[stock] * quantity
    result = f"Total investment in {stock}: ${total}"
    print(result)
    with open("investment.txt", "w") as f:
        f.write(result)
    print("Investment details saved to 'investment.txt'.")
else:
    print("Stock not found.")
