##Health Information System API##
A Django REST API for managing healthcare clients and programs. This system allows healthcare providers to create health programs, register clients, enroll clients in programs, search for clients, and view client profiles.
Features

Create and manage health programs (TB, Malaria, HIV, etc.)
Register new clients in the system
Enroll clients in one or more health programs
Search for clients by name or contact information
View detailed client profiles with program enrollments
RESTful API for integration with other systems

##Technology Stack

Django 4.2+
Django REST Framework
SQLite (development) / PostgreSQL (production)

""Installation and Setup""

##Clone the repository

git clone https://github.com/yourusername/health-system-api.git
cd health-system-api

##Create and activate a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows: ./venv/Scripts/activate

##Install dependencies

pip install -r requirements.txt

##Run migrations

python manage.py makemigrations health_core
python manage.py migrate

##Create a superuser##

python manage.py createsuperuser

##Run the development server

python manage.py runserver

Access the Swagger at  http://127.0.0.1/8000/
Access the API at http://127.0.0.1:8000/api/
Access the admin at http://127.0.0.1:8000/admin/
