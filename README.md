# [Find a Date](https://project3-mongo.herokuapp.com/)

## Introduction

Find a date is an online dating platform that allows user to connect with other users all over the world. Users can create a profile on the platform and view profiles of other users that they are interested in. 


The website allows users to interact and perform CRUD operations. It uses a non-relational database ([MongoDB](https://www.mongodb.com/)). Python and Flask is used to retrieve the list of profiles, filter and show profiles based on various criteria. 


## Demo

The deployed version of the website can be found at https://project3-mongo.herokuapp.com/.

![Demo](https://s5.gifyu.com/images/2019-11-08-23.10.03.gif)


| Contents                          |
|-----------------------------------|
|[UX](#ux)                          |
|[Features](#features)              |
|[Technologies Used](#technologies-used)|
|[Testing](#testing)                |
|[Deployment](#deployment)          |
|[Credits](#credits)                |



## UX


### Strategy

The website was designed to be visually appealing and minimalistic. 
Orange was chosen as the theme colour as it gives a fun and cheerful vibe to the website.


Users are able to:
* Create a new profile with the function to upload image
* Read the list of dating profiles easily
* Update the profile details and images
* Delete profiles
* Filter and view dating profiles by categories



### User Stories

As a user, I want to be able to: 
* View and navigate the website easily on my computer and mobile devices
* Have quick access to all the dating profiles available on the website
* Add a profile and upload my profile image easily
* Make changes and delete my dating profile easily
* Filter the dating profiles by the criteria I have set



## Features


### Existing Features

* Navigation Bar/ Dropdown Menu

 * The navigation bar was created using [Materialize](https://materializecss.com/navbar.html). 
 * The navigation bar is mobile responsive as it toggles a dropdown menu when the website is in mobile view. Users do not have to use back-button or scroll up to the top to use the navigation bar.


* Filter Profiles function

 * Users are able to filter profiles based on different categories under the Search Profiles page.


* Responsive card format

 * The profiles are displayed in card format using [Materialize](https://materializecss.com/cards.html). 
 *This format helps to keep the website minimalistic as it only displays the profiles’ key information. The rest of the profiles’ information will only be revealed when the card is clicked. 


### Features Left to Implement

* User Registration and Login

 * Currently, anyone can edit and delete profiles that do not belong to them. User Registration and Login will allow user to only edit and delete their own profile.

* Better Search and Filter function

 * Currently, the filter function only caters for a few categories. A more robust search and filter function could be implemented in the future. 

* Like Function 

 * A like function could be added to allow users to like the profiles they are interested in. 

* Chat Room

 * A chat room could be added to allow users to communicate with other users on the website.


## Technologies Used

HTML

CSS

Javascript

jQuery

Python

[Flask](https://www.palletsprojects.com/p/flask/)

[MongoDB](https://www.mongodb.com/)

[Materialize](https://materializecss.com/)

[Heroku](https://heroku.com/)


## Testing

Testing was done manually for all CRUD functions and also for all buttons and forms. Chrome developer tools was used for all testing to make sure that the website is mobile responsive.


## Deployment

The project was written on AWS Cloud9 and was saved and tested locally. 

The website was hosted through Heroku and is deployed from the master branch so that it can be updated through new commits to the master branch. 

Regular commits were performed and pushed to Heroku which allows ease of tracking for any changes to the codes.


## Credits

### Content

All images were sourced from [Pexels](https://www.pexels.com/).


**This site has been created for educational purposes only**
