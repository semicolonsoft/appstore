#!/bin/sh

python manage.py migrate >> /migrations.log
exec "$@"
