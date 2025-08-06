from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def he():
    return "Homes"

# GET - USED TO GET DATA
# POST - USED TO PUT DATA
# PUT - USED TO MODIFY THE ALREADY PRESENT DATA
# DELETE - USED TO DELETE DATA

if __name__ == "__main__" :
    app.run()