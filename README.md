### О проекте:
Платформа для онлайн-обучения, на которой каждый желающий сможет размещать свои полезные материалы или курсы.

### Технологический стек:
- Python
- Django
- PostgreSQL
- Redis
- Celery
- Docker
- Для подробного ознакомления посмотрите pyproject.toml

### Инструкция по запуску проекта через docker-compose:
1. git clone https://github.com/ataraksiia/Django_REST_Framework.git
2. cd Django_REST_Framework
3. Заполните .env по шаблону .env.sample
4. docker-compose up -d --build
5. python manage.py migrate
6. python manage.py createsuperuser
7. python manage.py runserver

### Чтобы проверить работоспособность каждого сервиса, можете:
* Для бэкенда отправить тестовый запрос к API 
* Для базы данных  выполнить SQL-запрос.
* Для Redis записать и прочитать данные. 
* Для Celery и Celery Beat запустить задачу.
