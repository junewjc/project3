from flask import Flask, render_template, request, redirect, url_for, flash
import os
from flask_pymongo import PyMongo, pymongo
import re
from bson.objectid import ObjectId 



MONGO_URI = os.getenv('MONGO_URI')
DATABASE_NAME = "projectDB"
COLLECTION_NAME = "profile"

def get_connection():
    conn = pymongo.MongoClient(MONGO_URI)
    return conn
    

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def index():
    conn = get_connection()
    profiles = conn[DATABASE_NAME][COLLECTION_NAME].find()
    return render_template('index.template.html', profiles=profiles)
    
@app.route('/add_profile')
def add_profile():
    return render_template('add_profile.template.html')
    
@app.route('/add_profile', methods=['POST'])
def insert_profile():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    gender = request.form.get('gender')
    age = request.form.get('age')
    occupation = request.form.get('occupation')
    country = request.form.get('country')
    religion = request.form.get('religion')
    race = request.form.get('race')
    hobby = request.form.get('hobby')
    email = request.form['email']
    phone = request.form.get('phone')
    summary = request.form.get('summary')
    
    conn = get_connection()
    conn[DATABASE_NAME][COLLECTION_NAME].insert({
        "first_name" : first_name,
        "last_name" : last_name,
        "gender" : gender,
        "age" : age,
        "occupation" : occupation,
        "country" : country,
        "religion" : religion,
        "race" : race,
        "hobby" : hobby,
        "email" : email,
        "phone" : phone,
        "summary" : summary
    })
    flash("You have added a new profile.")
    return redirect("/")
    
@app.route('/edit_profile/<profile_id>')
def show_edit_profile(profile_id):
    conn = get_connection()
    profile = conn[DATABASE_NAME][COLLECTION_NAME].find_one({
        '_id': ObjectId(profile_id)
    })
    return render_template('edit_profile.template.html', profile=profile)
    
@app.route("/edit_profile/<profile_id>", methods=['POST'])
def process_edit_profile(profile_id):
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    gender = request.form.get('gender')
    age = request.form.get('age')
    occupation = request.form.get('occupation')
    country = request.form.get('country')
    religion = request.form.get('religion')
    race = request.form.get('race')
    hobby = request.form.get('hobby')
    email = request.form['email']
    phone = request.form.get('phone')
    summary = request.form.get('summary')
    
    conn = get_connection()
    conn[DATABASE_NAME][COLLECTION_NAME].update({
        '_id':ObjectId(profile_id)
    }, {
        "first_name" : first_name,
        "last_name" : last_name,
        "gender" : gender,
        "age" : age,
        "occupation" : occupation,
        "country" : country,
        "religion" : religion,
        "race" : race,
        "hobby" : hobby,
        "email" : email,
        "phone" : phone,
        "summary" : summary
    })
    flash("The profile has been updated.")
    return redirect("/")
    
@app.route('/delete_profile/<profile_id>')
def delete_profile(profile_id):
    conn = get_connection()
    profile = conn[DATABASE_NAME][COLLECTION_NAME].remove({
        '_id': ObjectId(profile_id)
        
    })
    return redirect("/")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
