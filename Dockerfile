# Шаг 1: Используем базовый образ с установленным Python
FROM python:3.12-alpine

RUN apt-get update && apt-get install -y git

# Клонируем репозиторий с GitHub
RUN git clone https://github.com/maxempolk/fastapi-app.git /app

# Шаг 2: Устанавливаем рабочую директорию
WORKDIR /app

# Шаг 3: Копируем файл зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Шаг 4: Копируем исходный код приложения
COPY . .

# Шаг 5: Указываем команду для запуска приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]