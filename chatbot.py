import datetime
import random

# Joke list
jokes = [
    "Why did the computer get cold? Because it forgot to close its Windows!",
    "Why don’t programmers like nature? It has too many bugs.",
    "I told my computer I needed a break, and now it won’t stop sending me KitKat ads.",
    "Why was the JavaScript developer sad? Because he didn't Node how to Express himself.",
]

def get_time():
    return datetime.datetime.now().strftime("%I:%M %p")

def get_date():
    return datetime.datetime.now().strftime("%A, %d %B %Y")
def get_day():
    return datetime.datetime.now().strftime("%A, %d %B %Y")

def chatbot_response(user_input, user_name):
    user_input = user_input.lower().strip()

    # Greetings
    if user_input in ['hello', 'hi', 'hey']:
        return f"Hi {user_name}! How can I help you?"
    
    # How are you
    elif user_input in ['how are you', 'how are you doing']:
        return "I'm just a bunch of Python code, but I'm happy to chat with you! 😊"
    
    # Time
    elif 'time' in user_input:
        return f"The current time is {get_time()}."
    
    # Date
    elif 'date' in user_input or "day" in user_input:
        return f"Today's date is {get_date()}."
    
    # Name
    elif 'your name' in user_input:
        return "I'm PyBot, your friendly Python chatbot!"
    
    # Joke
    elif 'joke' in user_input:
        return random.choice(jokes)
    
    # Thank you
    elif user_input in ['thanks', 'thank you']:
        return "You're most welcome!"
    
    # Goodbye
    elif user_input in ['bye', 'goodbye', 'see you']:
        return "bye"
    
    # Unknown
    else:
        return "I'm not sure how to respond to that. Try asking something else!"

def start_chat():
    print("🤖 PyBot: Hello! What's your name?")
    user_name = input("🧑 You: ").strip().title()

    print(f"🤖 PyBot: Nice to meet you, {user_name}! Type something to chat. Type 'bye' to exit.")

    while True:
        user_input = input(f"🧑 {user_name}: ")

        response = chatbot_response(user_input, user_name)

        if response == "bye":
            confirm = input("🤖 PyBot: Are you sure you want to exit? (yes/no): ").lower().strip()
            if confirm in ['yes', 'y']:
                print("🤖 PyBot: Goodbye! Have a great day!")
                break
            else:
                continue

        print(f"🤖 PyBot: {response}")

# Start the chatbot
if __name__ == "__main__":
    start_chat()
