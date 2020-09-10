# My school


## Запуск проекта
1. cd my_school 
2. python manage.py migrate
3. python manage.py add_test_data
4. python manage.py createsuperuser
5. docker run -p 0.0.0.0:6379:6379 redis (Запуск redis)
6. python manage.py rqworker default (Запуск rq)
7. python manage.py runserver


## JWT 
curl \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"username": "admin", "password": "admin"}' \
    http://127.0.0.1:8000/api/token/