from flask import Flask, request, jsonify
import json
import pandas as pd
from datetime import datetime
from zoneinfo import ZoneInfo
import uuid 
import os

# Init the database location
DATA_FILE="Data/users.json"
os.makedirs('Data', exist_ok=True)

# Ensure users.json exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f, indent=4)

app = Flask(__name__)

@app.route("/get-user/<uid>")
def getUser(uid):

    # Loads the file
    try:
        with open(DATA_FILE, "r") as f:
            users = json.load(f)
    except FileNotFoundError:
        return jsonify({"error": "No user database found"}), 404
    
    # Check and return User info
    for user in users:
        if user.get("uid") == uid:
            return (jsonify(user), 200)

    # If User not found
    return jsonify({"error": f"User with id '{uid}' not found"}), 404

@app.route("/create-user", methods=["POST"])
def createUser():
    data = request.get_json()

    # INITIALIZING THE DATA
    userName = data["userName"]
    data["userName"] = userName

    password = data["password"]
    data["password"] = password

    email = data["email"]
    data["email"] = email

    data["uid"] = f"user_{datetime.now(ZoneInfo('Asia/Kolkata')).strftime('%Y-%m-%d_%H-%M-%S')}_{uuid.uuid4().hex[:8]}"
    data["createdAt"] = datetime.now(ZoneInfo('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')

    # Load existing data
    with open(DATA_FILE, 'r') as f:
        users = json.load(f)

    # Append new user
    users.append(data)

    # SAVES TO FILE
    with open(DATA_FILE, 'w') as f:
        json.dump(users, f, indent=4)

    return jsonify(users), 201


if __name__ == "__main__" :
    app.run()

# GET - USED TO GET DATA
# POST - USED TO PUT DATA
# PUT - USED TO MODIFY THE ALREADY PRESENT DATA
# DELETE - USED TO DELETE DATA
