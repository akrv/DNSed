import hashlib
import os

from flask import Flask, request, jsonify
from flask_jsonschema import JsonSchema, ValidationError
from databse import do_the_registration
app = Flask(__name__)

#JSON Validation
app.config['JSONSCHEMA_DIR'] = os.path.join(app.root_path, 'schemas')
jsonschema = JsonSchema(app)

@app.errorhandler(ValidationError)
def on_validation_error(e):
    return jsonify(send_back_prototype(reason="JSON schema parse error"))

def send_back_prototype(reason):
    message = {
                "status" : "error",
                "allowed": "only post methods are allowed",
                "reason": reason
    }
    return message

def get_remote_addr(request_data):
    # find the IP address that the client is requesting from
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr
    return ip

@app.route("/register", methods=['GET', 'POST'])
@jsonschema.validate('register', 'create')
def register_endpoint():
    #TODO jsonschema matching
    if request.method == 'POST':
        request_json = request.get_json()

        # generating tokens
        request_json['token'] = hashlib.sha1(os.urandom(128)).hexdigest()

        #tagging the remote ip
        request_json['ip_address'] = get_remote_addr(request_data=request)

        print (request_json)
        #return do_the_registration()
        return 'OK'
    else:
        return jsonify(send_back_prototype(reason="this endpoint accepts only POST method"))

if __name__ == "__main__":
    app.run()