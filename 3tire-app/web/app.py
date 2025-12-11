from flask import Flask, jsonify, request
import os
import psycopg2

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "db")
DB_NAME = os.environ.get("DB_NAME", "appdb")
DB_USER = os.environ.get("DB_USER", "appuser")
DB_PASS = os.environ.get("DB_PASS", "password")

@app.route('/')
def home():
    return "Welcome to the 3-Tier Dockerized App!"

@app.route('/data')
def get_data():
    conn = psycopg2.connect(
        host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM students;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
