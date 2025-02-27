from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# MySQL Configuration
app.config["MYSQL_HOST"] = 'localhost'
app.config["MYSQL_USER"] = 'root'
app.config["MYSQL_PASSWORD"] = 'awan'
app.config["MYSQL_DB"] = 'EasyBook'

def get_db_connection():
    conn = mysql.connector.conenct(
        host = app.config['MYSQL_HOST'],
        user = app.config['MYSQL_USER'],
        password = app.config['MYSQL_PASSWORD'],
        database = app.config['MYSQL_DB']
    )
    return conn

# Route to hompage
@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug="True")