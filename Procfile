release: python manage.py makemigrations gram
release: python manage.py migrate

web: gunicorn el_gram.wsgi --log-file -
