## Done by Abylai Aitbanov 19B030059
## E-commerce store for online shopping

An E-commerce  online store is a website through which customers  can place orders and individuals buy and sell goods and services over the Internet

Products are divided by categories, though so users can get the product they want. By creating your account(client) you will have access to your card, cart, profile, and orders that you will purchase.


## Getting started
### Clone the repository to your local machine:
* Create and activate a virtual environment:
* python3 -m venv venv
* source env/bin/activate
### Install necessary packages
* pip install -r requirements.txt

### Configure database in settings.py
### DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your_db_name',
        'USER': 'your_username',
        'PASSWORD': 'your_pasword',
        'HOST': 'localhost',
        'PORT': '5432',
    }}

### Run database migrations:

* python manage.py makemigrations
* python manage.py migrate


### Create a superuser:
* python manage.py createsuperuser
### Run the API server
* python manage.py runserver
