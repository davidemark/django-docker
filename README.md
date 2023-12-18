# Django-Docker Project

## Steps:
- python -m venv venv
- source/venv/bin/activate
- pip install django
- pip install djangorestframework
- django-admin startproject my_project .
- python manage.py migrate
- python manage.py startapp my_app
- add 'my_app' and 'rest_framework' in INSTALLED_APPS in settings.py
- add models in models.py
- python manage.py makemigrations my_app
- python manage.py migrate my_app
- add views in views.py and create urls.py in my_app
- python manage.py runserver - for testing
- pip freeze > requirements.txt
- deactivate - for deactivate the virtual environment
- create .dockerignore .gitignore, Dockerfile and docker-compose.yml in root folder

