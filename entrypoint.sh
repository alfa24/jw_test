#!/usr/bin/env bash

python manage.py migrate --noinput
python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL

exec "$@"
