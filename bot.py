from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

def send_message(output):
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(output)
    return str(resp)

@app.route('/')
def say_hello():
    return "<h2>Welcome to my E-Commerce bot</h2>"

@app.route('/bot', methods=['POST'])
def bot():
    user_input = request.values.get('Body', '').lower()
    remote_number = request.values.get("From", "")

    if remote_number.startswith("whatsapp:"):
        remote_number = remote_number.split(":")[1]

    greetings = ["hello", "hi", "good morning", "good afternoon", "good evening", "good afternoon", "whats up", "how far"]

    if any(word.startswith(user_input) for word in greetings):
        output = """
Hello, welcome to my E-commerce platform:
What will you like to do today?
A. Check my account
B. Track my order
C. View products
D. Lodge a complain
"""
        return send_message(output)

    if user_input == 'a':
        output = """
Is this the phone number associated with your account?
Y. Yes
N. No
"""
        return send_message(output)

    if user_input == 'y':
        output = f"your phone number is {remote_number}: \nYou currently have no products to be checked out"
        return send_message(output)

    if user_input == 'n':
        output = """
You have some products to be checked out
"""
        return send_message(output)
    
    else:
        output = """
I don't seem to understand your message, please try again
"""
        return send_message(output)

if __name__ == '__main__':
    app.run()

