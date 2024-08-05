# UTF.tech Backend

## Описание

Реализовано представление, которое возвращает список категорий с опубликованными блюдами. Для каждой категории в ответе включаются только те блюда, которые опубликованы. В API реализован фильтр, чтобы в выборку попадали только те категории, которые содержат хотя бы одно опубликованное блюдо.

## Стек технологий

- Django 4.2.14
- Django REST Framework 3.15.2
- PostgreSQL 14.12

## Установка

1. Клонируйте репозиторий

    ```bash
    git clone git@github.com:twsomt/UTF.tech.git
    cd UTF.tech
    ```

2. Создайте и активируйте виртуальное окружение

    ```bash
    python -m venv venv
    source venv/bin/activate  # На Windows используйте `venv\Scripts\activate`
    ```

3. Установите зависимости

    ```bash
    pip install -r requirements.txt
    ```

4. Настройте базу данных

   Создайте файл .env и укажите в нем необходимые данные для подключения к PostgreSQL.
   Или отредактируйте данные в настройках проекта.

6. Примените миграции

    ```bash
    python3 manage.py migrate
    ```

7. Создайте суперпользователя

    ```bash
    python3 manage.py createsuperuser
    ```

8. Запустите сервер

    ```bash
    python3 manage.py runserver
    ```

## API

### Получение категорий блюд

Получить список всех категорий с опубликованными блюдами:

**URL:** `/api/v1/foods/`

**Метод:** `GET`

**Ответ:**

```json
[
    {
        "id": 1,
        "name_ru": "Напитки",
        "name_en": null,
        "name_ch": null,
        "order_id": 10,
        "foods": [
            {
                "internal_code": 100,
                "code": 1,
                "name_ru": "Чай",
                "description_ru": "Чай 100 гр",
                "description_en": null,
                "description_ch": null,
                "is_vegan": false,
                "is_special": false,
                "cost": "123.00",
                "additional": [
                    200
                ]
            },
            {
                "internal_code": 200,
                "code": 2,
                "name_ru": "Кола",
                "description_ru": "Кола",
                "description_en": null,
                "description_ch": null,
                "is_vegan": false,
                "is_special": false,
                "cost": "123.00",
                "additional": []
            }
        ]
    },
    {
        "id": 2,
        "name_ru": "Выпечка",
        "name_en": null,
        "name_ch": null,
        "order_id": 20,
        "foods": [
            {
                "internal_code": 300,
                "code": 3,
                "name_ru": "Пирог",
                "description_ru": "Вкусный пирог",
                "description_en": null,
                "description_ch": null,
                "is_vegan": true,
                "is_special": true,
                "cost": "250.00",
                "additional": []
            }
        ]
    }
]
