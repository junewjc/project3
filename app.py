from flask import Flask, render_template, request, redirect, url_for, flash
import os
from flask_pymongo import PyMongo, pymongo
import re
from bson.objectid import ObjectId 
from flask_uploads import UploadSet, IMAGES, configure_uploads


app = Flask(__name__)

MONGO_URI = os.getenv('MONGO_URI')
DATABASE_NAME = "projectDB"
COLLECTION_NAME = "profile"
conn = pymongo.MongoClient(MONGO_URI)

TOP_LEVEL_DIR = os.path.abspath(os.curdir) 
upload_dir = '/static/uploads/img/' 
app.config["UPLOADS_DEFAULT_DEST"] = TOP_LEVEL_DIR + upload_dir 
app.config["UPLOADED_IMAGES_DEST"] = TOP_LEVEL_DIR + upload_dir 
app.config["UPLOADED_IMAGES_URL"] = upload_dir 
app.secret_key = "secret"

images_upload_set = UploadSet('images', IMAGES)
configure_uploads(app, images_upload_set)


@app.route('/') #Homepage
def index():
    profiles = conn[DATABASE_NAME][COLLECTION_NAME].find().sort([("_id", -1)])
    return render_template('index.template.html', profiles=profiles)
    
@app.route('/search_profile') #Search profile page
def search_profile():
    gender = request.args.get('gender')
    race = request.args.get('race')
    religion = request.args.get('religion')
    critera= {} 
    
    if gender and gender != 'Gender':
        critera['gender'] = gender
    else:
        gender = 'Gender'
        
    if race and race != 'Race':
        critera['race'] = race
    else:
        race = 'Race'
        
    if religion and religion != 'Religion':
        critera['religion'] = religion
    else:
        religion = 'religion'
        
        
    profiles = conn[DATABASE_NAME][COLLECTION_NAME].find(critera)
    print(profiles)
    return render_template("search_profile.template.html", 
                           profiles=profiles, gender=gender, race=race, religion=religion)
    
@app.route('/add_profile') #Add profile page
def add_profile():
    return render_template('add_profile.template.html')
    
@app.route('/add_profile', methods=['POST']) #To add the new profile to mongodb database
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
    image = request.files.get('image') 
    filename = images_upload_set.save(image) 
    
    
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
        "summary" : summary, 
        "image_url" : images_upload_set.url(filename)
    })
    flash("You have added a new profile.")
    return redirect("/")
    
@app.route('/edit_profile/<profile_id>') #Edit profile page
def show_edit_profile(profile_id):
    profile = conn[DATABASE_NAME][COLLECTION_NAME].find_one({
        '_id': ObjectId(profile_id)
    })
    return render_template('edit_profile.template.html', profile=profile)
    
@app.route("/edit_profile/<profile_id>", methods=['POST']) #To update the profile details in mongodb database
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
    image = request.files.get('image') 
    filename = images_upload_set.save(image) 
    
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
        "summary" : summary, 
        "image_url" : images_upload_set.url(filename)
    })
    flash("The profile has been updated.")
    return redirect("/")
    
@app.route('/delete_profile/<profile_id>') #To delete profile
def delete_profile(profile_id):
    profile = conn[DATABASE_NAME][COLLECTION_NAME].remove({
        '_id': ObjectId(profile_id)
        
    })
    flash("The profile has been deleted.")
    return redirect("/")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
