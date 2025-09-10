from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Get MONGO_URI from .env
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["TramMongoDB1"]
todo_collection = db["todo_items"]   # new collection for To-Do items

@app.route("/")
def home():
    return "Welcome! Go to /todo to add To-Do items."

# ✅ To-Do form page
@app.route("/todo")
def todo_page():
    return render_template("todo.html")

# ✅ Backend to handle form submission
@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    try:
        item_name = request.form.get("itemName")
        item_description = request.form.get("itemDescription")

        # Insert into MongoDB
        todo_collection.insert_one({
            "itemName": item_name,
            "itemDescription": item_description
        })

        return f"✅ To-Do item saved: {item_name} - {item_description}"
    except Exception as e:
        return f"❌ Error saving To-Do item: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)

