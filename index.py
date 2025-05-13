from flask import Flask, redirect, render_template
from constants import messages, br_messages
from random import choice

app = Flask(__name__)

@app.route('/')
def home():
  return "Good to see you here!\nPlease, go to the route '/message' to see positive affirmations!"

@app.route('/message')
def message():
   random_message = choice(messages)
   return random_message

@app.route('/message/br')
def message_br():
   random_message = choice(br_messages)
   return random_message

if __name__ == '__main__':
   app.run(debug=True)