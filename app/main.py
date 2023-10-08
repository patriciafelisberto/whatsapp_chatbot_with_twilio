from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from .dispatch import BotDispatcher, QuizzManager


app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    original_msg = request.values.get('Body', '')

    dispatcher = BotDispatcher()
    botresponse = dispatcher.reply(original_msg)
    if botresponse == BotDispatcher.QUIZZ_FLOW:
        userid = request.values.get('WaId', None)
        quizzmanager = QuizzManager()
        botresponse = quizzmanager.reply(userid, original_msg)

    resp = MessagingResponse()
    msg = resp.message()

    msg.body(botresponse['body'])
    if botresponse.get('media', None):
        msg.media(botresponse['media'])
    print(str(resp))
    return str(resp)

@app.route('/')
def index():
    return "That's my Whatsapp chatbot application."
