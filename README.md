![example workflow](https://github.com/Vladislavhgtech/foodgram-project-react/actions/workflows/main.yml/badge.svg)

# Рабочий проект находится 
http://51.250.5.68/

Администратор: 
login: admin
pass: admin

Пользователь:
login: mskvldmsk@gmail.com
pass: 12345


# Описание.

Проект «Продуктовый помощник». На этом сервисе пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

Стек: Python 3, Django 3, Django REST Framework, SQLite3, PostgreSQL, gunicorn, nginx, Яндекс.Облако (Ubuntu 20.04)

# Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Vladislavhgtech/foodgram-project-react.git

```
```
cd foodgram-project-react
```
Создайте файл .env командой touch .env. Шаблон наполнения env-файла:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres_user
POSTGRES_PASSWORD=postgres_password
DB_HOST=db
DB_PORT=5432
ENV=LOCAL

```
```
Запустите docker-compose командой sudo docker-compose up -d
```
Создайте миграции: 
```
docker-compose exec backend python manage.py migrate --noinput
```
Соберите статику проекта командой:
```
sudo docker-compose exec web python manage.py collectstatic --no-input
```
Создайте суперпользователя Django:
```
sudo docker-compose exec web python manage.py createsuperuser
```
Загрузите тестовые данные в базу данных командой: 
```
sudo docker -compose exec backend python manage.py loaddata dump.json
```
### Над проектом работали: 
- Frontend - https://github.com/yandex-praktikum/foodgram-project-react
- Backend - https://github.com/Vladislavhgtech/foodgram-project-react