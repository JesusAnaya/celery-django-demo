# celery-django-demo
Celery Django demo

## Run servers
First step is run a rabbitmq-server in your computer,
then run python servers in different consoles.

    * python manage.py runserver
    * python manage.py celeryd --concurrency=1
    * python manage.py celerycam --frequency=10.0

Or also you can install the heroku tool and run all services usin:
    `heroku local`

Download heroku tools here: https://devcenter.heroku.com/articles/heroku-command-line

## Notes
The third party library `sorl-thumbnail` doesn't works good with Django 1.9,
it's necessary run this lines to force the last upgrade

`pip install --pre --upgrade sorl-thumbnail`

