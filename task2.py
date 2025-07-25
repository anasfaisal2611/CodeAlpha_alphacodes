class ChatBot:
    def __init__(self, name="Bot"):
        self.name = name
        self.responses = {
            "hi": "Hello!",
            "hello": "Hi there!",
            "how are you": "I'm fine, thanks!",
            "what's your name": f"My name is {self.name}.",
            "bye": "Goodbye!",
            "help": "You can say: hi, hello, how are you, what's your name, bye"
        }
    def get_response(self, message):
        message = message.lower().strip()
        return self.responses.get(message, "I don't understand that.")
    def start(self):
        print(f"{self.name}: Hello! Type 'help' to see commands. Type 'bye' to exit.")
        while True:
            try:
                user_input = input("You: ").strip()
                if not user_input:
                    print(f"{self.name}: Please say something.")
                    continue
                response = self.get_response(user_input)
                print(f"{self.name}: {response}")
                if user_input.lower() == "bye":
                    break
            except (EOFError, KeyboardInterrupt):
                print(f"\n{self.name}: Goodbye! (Exited safely)")
                break
if __name__ == "__main__":
    my_bot = ChatBot("Buddy")
    my_bot.start()
