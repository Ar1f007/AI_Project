from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

chatbot = ChatBot('RoboChat')
custom_bot = ChatBot("RoboChat", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(custom_bot.storage)
english_bot = ChatBot("RoboChat", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot.storage)
trainer.train("chatterbot.corpus.custom")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(custom_bot.get_response(userText))


if __name__ == "__main__":
    app.run()
