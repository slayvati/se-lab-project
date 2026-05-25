from flask import Flask, render_template, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/birthdays")
def birthdays():

    conn = sqlite3.connect("birthdays.db")
    cursor = conn.cursor()

    today = datetime.now().strftime("%m-%d")

    cursor.execute("""
        SELECT name, image
        FROM birthdays
        WHERE birthday = ?
    """, (today,))

    data = cursor.fetchall()

    conn.close()

    result = []

    for row in data:
        result.append({
            "name": row[0],
            "image": row[1]
        })

    return jsonify(result)

app.run(debug=True)