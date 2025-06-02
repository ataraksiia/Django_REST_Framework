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
* Для базы данных выполнить SQL-запрос.
* Для Redis записать и прочитать данные. 
* Для Celery и Celery Beat запустить задачу.

### Развертывание на удалённом сервере (Ubuntu-based)
1. sudo apt update && sudo apt upgrade -y
2. sudo apt install docker.io docker-compose -y
3. настройте .env
4. sudo ufw allow 'Nginx Full'
   sudo ufw allow OpenSSH
   sudo ufw enable
5. docker-compose up --build -d


### CI/CD (GitHub Actions)
Используйте шаблон `.github/workflows/deploy.yml` для автоматического деплоя на сервер:
1. yaml
name: Deploy to VPS

on:
  push:
    branches: [main, master, dev]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Copy files to server
        uses: appleboy/scp-action@master
        with:
          host: ${{ secrets.SERVER_IP }}
          username: ${{ secrets.SERVER_USER }}
          key: ${{ secrets.SERVER_SSH_KEY }}
          source: "."
          target: "/home/${{ secrets.SERVER_USER }}/Django_REST_Framework"
      - name: Run deploy script via SSH
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.SERVER_IP }}
          username: ${{ secrets.SERVER_USER }}
          key: ${{ secrets.SERVER_SSH_KEY }}
          script: |
            cd Django_REST_Framework
            docker-compose down
            docker-compose pull
            docker-compose up --build -d

2. Заполните в настройках репозитория SECRET переменные 

