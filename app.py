from flask import Flask
from flask import request
from flask import jsonify
from flask_pymongo import pymongo
from bson import json_util
import ssl
import json
import uuid
from urllib.request import urlopen
import urllib
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

CONNECTION_STRING = "mongodb+srv://inigo:prueba@cluster0.0lpx0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING, ssl_cert_reqs=ssl.CERT_NONE)
db = client.get_database('flask_mongodb_atlas')
covid_collection = pymongo.collection.Collection(db, 'covid_collection')

@app.route("/")
def test():
#   covid_collection.insert_one({"name": "John"})
    return "Connected to the dataabase!"

@app.route("/cuestionario", methods=['POST'])
def create_cuestionario():
    data=request.json
    covid_collection.insert_one({"_id":str(uuid.uuid4()),"covid":data["covid"],"profesion":data["profesion"], "vacunado":data["vacunado"]})
    return "Cuestionario completado"

@app.route("/cuestionario/list",methods=['GET'])
def list_cuestionario():
    cuestionario = covid_collection.find()
    response=[todo for todo in cuestionario]
    return json.dumps(response, default=json_util.default)




