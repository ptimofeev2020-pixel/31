# LMS — 30.2 Сериализаторы

Продолжение LMS-проекта на Django REST Framework: вычисляемые и вложенные поля
в сериализаторах, модель платежей, фильтрация.

## Стек

- Python, Django 5.2
- Django REST Framework
- django-filter
- SQLite

## Что добавлено в 30.2

- В сериализатор курса добавлено поле `lesson_count` (через `SerializerMethodField`)
- В сериализатор курса добавлен вывод уроков вложенным сериализатором (`lessons`)
- Модель `Payment` (пользователь, дата оплаты, оплаченный курс/урок, сумма, способ оплаты)
- Фикстура `users/fixtures/payments.json` с тестовыми данными
- Эндпоинт списка платежей с фильтрацией и сортировкой

## Установка и запуск

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata payments.json
python manage.py runserver
```

## Эндпоинты

- `GET /courses/<id>/` — курс с `lesson_count` и вложенными уроками
- `GET /payments/` — список платежей, поддерживает:
  - сортировку по дате: `?ordering=payment_date` / `?ordering=-payment_date`
  - фильтр по курсу: `?paid_course=<id>`
  - фильтр по уроку: `?paid_lesson=<id>`
  - фильтр по способу оплаты: `?payment_method=cash` / `?payment_method=transfer`
- `GET /users/<id>/` — профиль с историей платежей
