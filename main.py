from flask import Flask, request, jsonify
import json
import pandas as pd
from datetime import datetime
from zoneinfo import ZoneInfo
import uuid 
import os

data = [
    {"uid": [f"user_{uuid.uuid4().hex}"],
    "userName": "askjd", 
    "password": "123",
    "email": "askjdaw@gmail.com",
    "createdAt": datetime.now(ZoneInfo('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')
    },
    
    {"uid": [f"user_{uuid.uuid4().hex}"],
    "userName": "askjd", 
    "password": "123",
    "email": "askjdaw@gmail.com",
    "createdAt": datetime.now(ZoneInfo('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')
    }

]

df = pd.DataFrame(data)
df.to_json('./data.json', orient="records", indent=4, index=False)
# df = pd.read_json('./data.json')

with open("data.json", "r") as f:
    dataJson = json.load(f)

app = Flask(__name__)

@app.route("/get-user/<user_id>")
def getUser(uid):
    user_data = {
        "uid": uid,
        "name": "John Doe", 
        "email": "johndoe@gmail.com" 
    }

    user_extra = request.args.get("extra")
    if user_extra:
        user_data["extra"] = user_extra

    # return jsonify(user_data), 200
    return jsonify(dataJson), 200

@app.route("/create-user", methods=["POST"])
def createUser():
    data = request.get_json()

    # FROM THE URL
    # http://127.0.0.1:5000/create-user?name=shreyas
    # user_name = request.args.get("name")
    # data["username"] = user_name

    # FROM THE POST
    # http://127.0.0.1:5000/create-user

    userName = data["userName"]
    data["userName"] = userName

    password = data["password"]
    data["password"] = password

    email = data["email"]
    data["email"] = email

    data["createdAt"] = datetime.now(ZoneInfo('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')

    data["uid"] = f"user_{datetime.now(ZoneInfo('Asia/Kolkata')).strftime('%Y-%m-%d_%H-%M-%S')}_{uuid.uuid4().hex[:8]}"

    # SAVES TO FILE
    df = pd.DataFrame([data])
    os.makedirs('Data', exist_ok=True)
    df.to_json("Data/users.json", orient="records", indent=4, index=False)

    return jsonify(data), 201


if __name__ == "__main__" :
    app.run()

# GET - USED TO GET DATA
# POST - USED TO PUT DATA
# PUT - USED TO MODIFY THE ALREADY PRESENT DATA
# DELETE - USED TO DELETE DATA
