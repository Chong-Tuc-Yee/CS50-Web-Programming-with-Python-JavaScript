## HarvardX CS50W: Web Programming with Python & JavaScript

Self Study on Harvard Computer Science Web Dev Course.

### Course's Link ###
See [here](https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript).

### Course Content ###
1. [Pset0 (HTML, CSS)](https://github.com/Chong-Tuc-Yee/HarvardX-CS50-Web-Programming-with-Python-JavaScript/tree/main/Pset0/search)
2. [Pset1 (Git)]()
3. [Pset2 (Python)]()
4. [Pset3 (Django)]()
5. [Pset4 (SQL, Models & Migrations)]()
6. [Pset5 (JavaScript)]()
7. [Pset6 (User Interfaces)]()
8. [Pset7 (Testing, CI/CD)]()
9. [Pset8 (Scalability & Security)]()

All webpages of the project are mobile-responsive.

Installation
Install project dependencies by running pip install -r requirements.txt. Dependencies include Django and Pillow module that allows Django to work with images.
For Django projects:
Make and apply migrations by running python manage.py makemigrations and python manage.py migrate.
Create superuser with python manage.py createsuperuser. This step is optional.
Go to website address and register an account.
Files and directories
djangoapp - main application directory.
static/djangoapp contains all static content.
css contains compiled CSS file and its map.
js - all JavaScript files used in project.
post.js - script that run in post.html template.
search.js - this script run in every template because it is included in base template. It validates the search field.
upload.js - script that run in upload.html template.
user.js - script that run in user.html template.
welcome.js - script that run in welcome.html template.
scss - source SCSS files.
templates/djangoapp contains all application templates.
_base.html - base templates. All other tempalates extend it.
_posts_list.html - subtemplate that is used in a couple of other templates with include directive. Contains HTML for posts lists.
_users_list.html - same as previous one but contains HTML for users lists.
followers.html and following.html - templates for users lists.
index.html - main templates that shows new photos feed (only for registered users).
post.html - template that shows a single post.
search.html - this template shows search result.
upload.html - template for uploading new photo.
user.html - this one shows user details.
welcome.html - main template for unregistered users. It shows login and registration forms.
admin.py - here I added some admin classes and re-registered User model.
models.py contains three models I used in the project. UserExtended model extends the standard User model, Post model is for posts, and Comment represents users comments.
urls.py - all application URLs.
views.py respectively, contains all application views.
djangogram - project directory.
media - this directory contains two default images (no_avatar.png and no_image.png), and here will be saved all users photos.
