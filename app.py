from flask import Flask
import os

app = Flask(__name__)

# Veritabanı bağlantı bilgilerini environment variables üzerinden al
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")
DB_HOST = os.environ.get("DB_HOST")

@app.route('/')
def home():
    return f"Merhaba SE4453 Final'den!<br><br>" \
           f"DB_USER: {DB_USER}<br>" \
           f"DB_NAME: {DB_NAME}<br>" \
           f"DB_HOST: {DB_HOST}"

@app.route('/hello')
def hello():
    return "Hello from Azure CI/CD!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
