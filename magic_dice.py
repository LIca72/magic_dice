import random

# List of magical answers
answers = [
    "Yes, definitely.",
    "Most likely, yes.",
    "Ask again later.",
    "Cannot predict now.",
    "Don't count on it.",
    "Hmm... it's possible!",
    "Try again.",
    "Absolutely not.",
    "Your intuition already knows.",
    "Absolutely yes!",
    "Something tells me... no."
]

# Main game loop
while True:
    question = input("🔮 Ask the Magic Dice a question (or type 'exit' to quit): ")
    if question.lower() == "exit":
        print("👋 Goodbye! The Magic Dice goes to sleep...")
        break
    print("🧿 The Magic Dice says:", random.choice(answers))
