## Introduction
This is a Django app that was made for Civil Department, IIT Indore but was not put under production.
### How to run
- Install Python3
- Clone the repository with ``` git clone https://github.com/jains8844/civil_iiti ```
- Run ``` pip install -r requirements.txt ```
- Make migrations with ``` python manage.py makemigrations ``` and ``` python manage.py migrate ```
- Run ``` python manage.py runserver ```
- The web app will be served at [localhost:8000](localhost:8000)
- The admin panel can be accessed by creating a superuser with ``` python manage.py createsuperuser ``` and accessed with [localhost:8000/admin](localhost:8000/admin)

### About

* The web app uses sqlite3 as its database.
* It provides a login system for the Faculties along with an admin panel using Django Admin.
* Homepage details and other things can be edited using the admin panel.

