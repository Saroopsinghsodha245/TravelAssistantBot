from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging

# Disable ChatterBot info logs
logging.basicConfig(level=logging.ERROR)

app = Flask(__name__)

# Create the chatbot
chatbot = ChatBot(
    'TravelAssistant',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ]
)

# Define conversation data
trainer = ListTrainer(chatbot)

conversation = [
    "Hello",
    "Hi there! How can I help you plan your travel today?",
    "Tell me a joke",
    "Why don’t mountains get cold in the winter? They wear snowcaps!",
    "I want to travel",
    "That’s great! Do you have a specific destination in mind?",
    "Which is the best country to visit?",
    "It depends on your interests! For beaches: Maldives, for culture: Italy, for nature: Switzerland.",
    "What are the best places to visit in Pakistan?",
    "Some amazing spots: Hunza Valley, Skardu, Fairy Meadows, Karachi, and Lahore Fort.",
    "Tell me about famous tourist attractions in Karachi",
    "Top attractions: Clifton Beach, Mazar-e-Quaid, Mohatta Palace, and Pakistan Maritime Museum.",
    "How can I book a flight?",
    "You can use websites like Skyscanner, Kayak, or Google Flights to compare and book tickets.",
    "What’s the best time to travel?",
    "The best travel times are usually spring (April–June) or autumn (October–November).",
    "Do I need travel insurance?",
    "Yes, many countries require travel insurance for visa or entry. It’s always recommended.",
    "Thank you",
    "You're very welcome! 😊 Safe travels!",
    "Goodbye",
    "Goodbye! Have a wonderful journey!"
]

trainer.train(conversation)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def get_bot_response():
    user_msg = request.form.get("msg")
    if not user_msg:
        return jsonify({"response": "Please type something so I can help you."})

    bot_response = str(chatbot.get_response(user_msg))
    return jsonify({"response": bot_response})


if __name__ == "__main__":
    app.run(debug=True)
