import os


DB_USERNAME = 'postgres'
DB_PASSWORD = 'Sriram%4086'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'postgres'

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database

# TODO IMPLEMENT DATABASE URL
#username = 'postgres'
#password = 'Sriram@86'
#host = 'localhost'
#port = '5432'
#DB_NAME = 'postgres'
SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
