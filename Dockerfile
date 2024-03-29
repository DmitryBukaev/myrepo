# Используйте базовый образ Python
FROM python:3.11

# Копируем текущую директорию в контейнер в папку /app
COPY . /app

# Устанавливаем зависимости Python
RUN pip install pyserial

# Устанавливаем рабочую директорию
WORKDIR /app

# Команда, которая будет выполнена при запуске контейнера
CMD ["python", "bot.py"]
