Проект является API, предоставляющий контакт к приложению в виде социально сети. 
Функционал:
```
api/v1/jwt/create/ (POST): передаём логин и пароль, получаем токен.
api/v1/jwt/refresh/ (POST): передаём refresh-значение, получаем новый токен.
api/v1/jwt/verify/ (POST): передаём токен, получаем статус.
api/v1/posts/ (GET, POST): получаем список всех постов или создаём новый пост.
api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост по id.
api/v1/groups/ (GET): получаем список всех групп.
api/v1/groups/{group_id}/ (GET): получаем информацию о группе по id.
api/v1/posts/{post_id}/comments/ (GET, POST): получаем список всех комментариев поста с id=post_id или создаём новый, указав id поста, который хотим прокомментировать.
api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий по id у поста с id=post_id.
api/v1/follow/ (GET, POST): получаем подписки на авторов или подписываемся на нового.
```
Допуск к запросам имеет только авторизированный пользователь(по токену), редактировать и удалять посты/комментарии/подписки имеет право только автор.

## Как запустить проект:

В терминале, перейдите в каталог, в который будет загружаться приложение:
```
cd 
```

Клонируйте репозиторий:
```
git clone git@github.com:VladislavYar/api_final_yatube.git
```

Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```

* Если у вас Linux/macOS
    ```
    source venv/bin/activate
    ```

* Если у вас windows
    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выпоните миграции:
```
python manage.py makemigrations
python manage.py migrate
```

Создайте суперюзера (логин\почта\пароль):
```
python manage.py createsuperuser
```
Соберите статические файлы:
```
python manage.py collectstatic --no-input
```
Запуск проект:
```
python manage.py runserver
```

## Cтек проекта
Python v3.9, Django, DRF
