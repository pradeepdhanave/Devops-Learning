from flask import Flask, request, jsonify
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# MongoDB Connection
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["TramMongoDB1"]
todos_collection = db["todos"]

@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    try:
        item_name = request.form.get("itemName")
        item_description = request.form.get("itemDescription")

        if not item_name or not item_description:
            return jsonify({"error": "Both fields are required"}), 400

        todos_collection.insert_one({
            "itemName": item_name,
            "itemDescription": item_description
        })

        return jsonify({"message": "To-Do item added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=7000)

