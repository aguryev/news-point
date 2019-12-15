# News Point

## Description
News Point is a simple news site built using the Django framework.
There are 3 groups of users on the site: 'admins', 'editors' and 'users'. Any registered user may to post news articles. The articles posted by 'users' are moderated by 'admins' before publishing. The articles posted by 'editors' or 'admins' are published at once.
Any registered user may comment on any published post.

## Requirements
	django>=2.2.5
	dj-database-url>=0.5.0
	whitenoise>=5.0.1
	django-allauth>=0.40.0
	django-anymail[mailgun]>=7.0.0
	django-tinymce4-lite>=1.7.5 
	celery>=4.3.0
	redis>=3.3.11
	gunicorn>=19.9.0

## Environment variables used
	SECRET_KEY - Django project secret key
	DEBUG = 0 or 1 - Django 'DEBUG' variable value
	DATABASE_URL - PostgreSQL database url
	MAILGUN_API_KEY - @mailgun privat api key
	MAILGUN_DOMAIN - @mailgun domain used to send emails
	MAILGUN_SMTP_LOGIN - default email address used to send notifications
	REDIS_URL - Redis url


## Running the application
	locally:
	$ python manage.py makemigrations
	$ python manage.py migrate
	$ docker build -t web:latest .
	$ docker run -d --name news-point -e "PORT=8765" -e "DEBUG=1" -p 8000:8765 web:latest

	heroku:
	$ heroku create news-point
	$ heroku container:login
	$ docker build -t registry.heroku.com/news-point/web .
	$ docker push registry.heroku.com/news-point/web
	$ heroku container:release web
	$ heroku addons:create heroku-postgresql:hobby-dev
	$ heroku run python manage.py makemigrations
	$ heroku run python manage.py migrate
