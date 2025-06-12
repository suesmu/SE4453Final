from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Merhaba SE4453 Final'den!"

@app.route('/hello')
def hello():
    return "Hello from Azure CI/CD!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
