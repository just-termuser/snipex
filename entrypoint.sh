#!/bin/bash

echo "Entrypoint script is running"
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
