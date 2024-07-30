docker-compose up -d --build
docker-compose exec app python manage.py migrate && python manage.py csu