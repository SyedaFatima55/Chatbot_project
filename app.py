from flask import Flask, render_template, request 
from datetime import datetime

app = Flask(__name__)

def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hi there! How can I help you?"
    elif "how are you?" in user_input:
        return "I'm an AI bot, but I'm doing great! How about you?"
    elif "What is your name?" in user_input:
        return "My name is ChatMate"
    elif "Weather?" in user_input:
        return "It's sunny outside"
    elif "what can you do?" in user_input:
        return "I can answer simple questions and keep you company!"
    elif "do you sleep?" in user_input:
        return "Nope, I'm always awake and ready to chat! "
    elif "how old are you?" in user_input:
        return "I'm timeless! Just born in the cloud. "
    elif "who made you?" in user_input:
        return "I was created by an awesome developer (Syeda Fatima)"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day!"
    elif "what is the time?" in user_input or "tell me the time" in user_input:
        now = datetime.now()
        current_time = now.strftime("%I:%M %p")  
        return f"The current time is {current_time}."
    else:
        return "Sorry, I didn't understand that."

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get', methods=['GET'])
def get_bot_response():
    user_text = request.args.get('msg')  
    bot_reply = get_response(user_text)
    return bot_reply

if __name__ == "__main__":
    app.run(debug=True)