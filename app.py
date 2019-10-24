from flask import Flask, render_template, request, redirect, url_for
import os
import pymongo
import re


# MONGO_URI = os.getenv('MONGO_URI')
# DATABASE_NAME = "projectDB"
# COLLECTION_NAME = "firstMDB"

# def get_connection():
#     conn = pymongo.MongoClient(MONGO_URI)
#     return conn

# app = Flask(__name__)

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
