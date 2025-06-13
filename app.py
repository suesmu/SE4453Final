from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Merhaba se4453 final'den!"

@app.route('/hello')
def hello():
    return "hello from azure ci/cd!"

@app.route('/db')
def db_connection():
    db_host = os.environ.get('dbhost')
    db_name = os.environ.get('dbname1')
    db_user = os.environ.get('dbuser1')
    db_password = os.environ.get('dbpassword1')



    # Sadece değişkenler dolu mu kontrol ediliyor
    if db_host and db_name and db_user and db_password:
        return "veritabanına başarıyla bağlanıldı."
    else:
       
        return "veritabanı bilgileri eksik!"

if __name__ == '__main__':
   

    app.run(host='0.0.0.0', port=80)
