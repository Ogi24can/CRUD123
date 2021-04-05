from flask import Flask, render_template
import pymongo
from pymongo import MongoClient
import json
from bson import json_util

cluster = MongoClient("mongodb+srv://Ogulcan:123ogulcan@cluster0.es5zn.mongodb.net/mydb?retryWrites=true&w=majority")

db = cluster["mydb"]
collection = db["sa"]

app = Flask(__name__)

# collection.insert_one({"name":"name"}) Eklemek için
# collection.delete_one({"name":"name"}) Silmek için
# collection.update_one({"name":"name"},{"$set": {"name":"new name"}}) Güncellemek için

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/veriekleme", methods=["POST"])
def add_veriler():
    request_payload = request.json
    name = request_payload["name"]
    print(request.json)
    collection.insert_one({"name":"name"})

@app.route("/veri", methods=["GET"])
def get_veriler():
    veriler = list(collection.find({}))
    return json.dumps(veriler, default=json_util.default)

@app.route("/verisilme", methods=["DELETE"])
def delete_Veriler():
    collection.delete_one({"name":"name"})
    return json.dumps(veriler, default=json_util.default)

