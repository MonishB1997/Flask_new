from flask import Flask, request, render_template
import os
import pymongo

MONGO_URI = os.getenv("MONGO_URI")
client = pymongo.MongoClient(MONGO_URI)
db = client.Monish
collection = db["TodoItems"]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# ✅ NEW API ROUTE
@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    item_name = request.form.get("itemName")
    item_description = request.form.get("itemDescription")

    if not item_name or not item_description:
        return "Item name or description cannot be empty", 400

    todo_data = {
        "itemName": item_name,
        "itemDescription": item_description
    }

    collection.insert_one(todo_data)
    return "To‑Do item submitted successfully"

if __name__ == "__main__":
    app.run(debug=True)
