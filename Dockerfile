# Указываем базовый образ
FROM python:3.11

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Устанавливаем Poetry
RUN pip install poetry

# Копируем файлы с зависимостями
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости с помощью Poetry
RUN poetry install --no-root

# Копируем остальные файлы проекта в контейнер
COPY README.md /app/README.md


# Открываем порт 8000 для взаимодействия с приложением
EXPOSE 8000

# Определяем команду для запуска приложения
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
