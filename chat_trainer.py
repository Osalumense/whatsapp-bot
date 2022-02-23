from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("E-Commerce-chatbot")
trainer = ListTrainer(chatbot)