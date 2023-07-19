import time
from flask import Flask, request, render_template
import keyboard

app = Flask(__name__)

history = []


@app.route('/')
def index():
    return render_template('index.html', history=history)


@app.route('/keyboard', methods=['POST'])
def keyboard_input():
    text = request.form['text']

    time.sleep(5)

    keyboard.write(text)

    if len(text) > 52:
        history.append(text[:50]+"...")
    else:
        history.append(text)

    return render_template('index.html', history=history)


if __name__ == '__main__':
    app.run()