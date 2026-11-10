from flask import Flask
from pymongo import MongoClient 

try:
    client = MongoClient("mongodb://mongo:27017")
    db = client["ma_database"]
    client.admin.command("ping")
    print("Successfully connected")

except Exception as e:
    print("Connection failed:", e)

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
    