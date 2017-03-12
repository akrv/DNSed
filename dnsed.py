import hashlib
import os
import datetime

from pymongo import MongoClient
from credentials import DEPLOY

if DEPLOY == 'dev':
    from credentials import MONGO_DEV as MONGO
elif DEPLOY == 'prod':
    from credentials import MONGO_DEV as MONGO
client = MongoClient(MONGO['host'], MONGO['port'])
db = client[MONGO['database']]

from flask import Flask, request, jsonify
from flask_jsonschema import JsonSchema, ValidationError

app = Flask(__name__)

# JSON Validation
app.config['JSONSCHEMA_DIR'] = os.path.join(app.root_path, 'schemas')
jsonschema = JsonSchema(app)

@app.errorhandler(ValidationError)
def on_validation_error(e):
    return "error"

def do_the_registration(req_json):
    # TODO put this function in another file, might help testing

    # generating tokens
    token = hashlib.sha1(os.urandom(128)).hexdigest()

    # put in database
    # return messsage with mongoID for object ID
    collection = db['devices']
    post = {"ip": "Mike",
             "text": "My first blog post!",
             "tags": ["mongodb", "python", "pymongo"],
             "date": datetime.datetime.utcnow()}
    post_id = posts.insert_one(post).inserted_id

def send_back_prototype():
    message = {
                "status" : "error",
                "reason" : "send the mac address of your device or something unique to the internet object to get a token.",
                "allowed": "only post methods are allowed"
    }
    return message

def get_remote_addr():
    # find the IP address that the client is requesting from
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr
    return ip

@app.route("/register", methods=['GET', 'POST'])
@jsonschema.validate('books', 'create')
def register_endpoint():
    #TODO jsonschema matching
    if request.method == 'POST':
        remote_addr = get_remote_addr()
        request.get_json()
        return do_the_registration()
    else:
        return jsonify(send_back_prototype())

if __name__ == "__main__":
    app.run()