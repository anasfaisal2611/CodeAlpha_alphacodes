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
