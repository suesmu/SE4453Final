from flask import Flask
import os

app = Flask(__name__)

# Key Vault üzerinden gelen environment değişkenlerini al
db_user = os.environ.get("dbuser1")
db_password = os.environ.get("dbpassword1")
db_name = os.environ.get("dbname1")
db_host = os.environ.get("dbhost")

@app.route('/')
def home():
    return f"""
        Merhaba SE4453 Final'den!<br><br>
        dbuser1: {db_user}<br>
        dbname1: {db_name}<br>
        dbhost: {db_host}
    """

@app.route('/hello')
def hello():
    return "Hello from Azure CI/CD!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
