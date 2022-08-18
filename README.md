# madklub-api SETUP

## Create venv (python version 3.9.12)

python3 -m venv venv
touch .env

Enter secret key into .env

source venv/bin/activate
source .env

pip install -r requirements

## Create local psql database

install postgres

sudo apt-get install postgresql postgresql-contrib

sudo -u postgres psql

CREATE DATABASE madklub;

CREATE USER madklubowner WITH PASSWORD 'madklub123';

ALTER ROLE madklubowner SET client_encoding to 'utf8';
ALTER ROLE madklubowner SET default_transaction_isolation TO 'read committed';
ALTER ROLE madklubowner SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE madklub TO madklubowner;

## Run migrations

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

## Access psql db

psql -U madklubowner -h 127.0.0.1 -d madklub
