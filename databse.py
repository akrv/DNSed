import datetime

from pymongo import MongoClient
from credentials import DEPLOY

if DEPLOY == 'dev':
    from credentials import MONGO_DEV as MONGO
elif DEPLOY == 'prod':
    from credentials import MONGO_DEV as MONGO
client = MongoClient(MONGO['host'], MONGO['port'])
db = client[MONGO['database']]

def do_the_registration(db_json):
    # TODO put this function in another file, might help testing

    # put in database
    # return messsage with mongoID for object ID
    collection = db['devices']
    post = {"ip": "Mike",
             "text": "My first blog post!",
             "tags": ["mongodb", "python", "pymongo"],
             "date": datetime.datetime.utcnow()}
