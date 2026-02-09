web: gunicorn InaDigi.wsgi
release: python manage.py migrate && python create_superuser.py && python compile_messages.py && python manage.py collectstatic --noinput