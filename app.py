from flask import Flask, render_template, request, redirect, url_for
import os
import pymongo
import re
from bson.objectid import ObjectId 


MONGO_URI = os.getenv('MONGO_URI')
DATABASE_NAME = "projectDB"
COLLECTION_NAME = "profile"

def get_connection():
    conn = pymongo.MongoClient(MONGO_URI)
    return conn

app = Flask(__name__)


@app.route('/')
def index():
    conn = get_connection()
    profiles = conn[DATABASE_NAME][COLLECTION_NAME].find()
    return render_template('index.template.html', profiles=profiles)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
