import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

data = [
    ("hello", "greeting"),
    ("hi", "greeting"),
    ("hey", "greeting"),
    ("how are you", "greeting"),
    ("bye", "goodbye"),
    ("goodbye", "goodbye"),
    ("see you", "goodbye"),
    ("what's up", "greeting"),
    ("how are you doing", "greeting"),
    ("tell me a joke", "joke"),
    ("tell me a story", "story"),
    ("what time is it", "time"),
    ("who are you", "information"),
    ("what is your name", "information")
]


X = [item[0] for item in data]
y = [item[1] for item in data]

model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(X, y)

responses = {
    "greeting": ["Hi there!", "Hello! How can I assist you?", "Hey! What's up?", "Hello, how can I help you today?"],
    "goodbye": ["Goodbye!", "See you later!", "Take care!", "Bye! Stay safe!"],
    "joke": ["Why don't skeletons fight each other? They don't have the guts!", "Why did the scarecrow win an award? Because he was outstanding in his field!"],
    "story": ["Once upon a time, in a land far away, there was a chatbot who loved to help people... Oh wait, that's me!"],
    "time": ["Sorry, I don't have access to the current time, but you can check your device for that!"],
    "information": ["I'm a chatbot, I don't have a personal name, but you can call me whatever you like!", "I'm your assistant, ready to chat!"]
}

def get_response(user_input):
    """Get the response based on the user input using the model."""
    intent = model.predict([user_input])[0]  
    return random.choice(responses.get(intent, ["I'm not sure what you mean. Can you rephrase?"]))

def run_chatbot():
    print("Welcome to the chatbot! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Take care!")
            break
        
        # Get and print chatbot's response
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    run_chatbot()
