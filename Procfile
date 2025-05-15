web: gunicorn config.wsgi --log-file -
release: python manage.py migrate && python manage.py load_initial_data