# Resource service

#### Сервис ресурсов команды moiami написанный на django.

##### Сущности сервиса:

​	MovieGetAction

​	Genre

​	Video

​	Image

​	Movie

​	Subscription

​	UserSubscription

​	User

​	Watchlist

### Эндпоинты:

#### 1. GET /api/v1/catalog/genres/

**Описание:** Получение списка всех жанров.

**Ответ:**

```
[
  { "id": "uuid", "name": "string" }
]
```

#### 2. POST /api/v1/catalog/genres/

**Описание:** Создание нового жанра.

**Тело запроса:**

json

```
{
  "name": "Новый жанр"
}
```



**Ответ:**

json

```
{
  "id": "uuid",
  "name": "Новый жанр"
}
```

#### 3. GET /api/v1/catalog/genres/{id}/

**Описание:** Получение информации о конкретном жанре.

**Параметры пути:** id  (UUID)

**Ответ:**

json

```
{
  "id": "uuid",
  "name": "string"
}
```

#### 4. GET /api/v1/catalog/images/

**Описание:** Список всех изображений.

**Ответ:**

json

```
[
  { "id": "uuid", "link": "url" }
]
```

#### 5. POST /api/v1/catalog/images/

**Описание:** Загрузка нового изображения. Поддерживает multipart/form-data, application/x-www-form-urlencoded.

**Тело запроса (multipart/form-data):**

​	file — файл изображения.

**Ответ:**

json

```
{
  "id": "uuid",
  "file": "путь к файлу",
  "link": "url"
}
```

#### 6. GET /api/v1/catalog/images/{id}/

**Параметры пути:** id (UUID)

**Ответ:**

json

```
{
  "id": "uuid",
  "file": "string",
  "link": "url"
}
```

#### 7. PUT /api/v1/catalog/images/{id}/

**Описание:** Обновление изображения.

**Параметры пути:**  id (UUID)

**Тело запроса (multipart/form-data):**

​	file — файл изображения.

**Ответ:** обновлённый объект.

#### 8. DELETE /api/v1/catalog/images/{id}/

**Описание:** Удаление изображения.

**Ответ:** пустое тело

#### 9. GET /api/v1/catalog/videos/

**Описание:** Список всех видео.

**Ответ:**

json

```
[
  { "id": "uuid", "link360": "url", "link1080": "url" }
]
```

#### 10. POST /api/v1/catalog/videos/

**Описание:** Загрузка нового видеофайла. Поддерживает multipart/form-data.

**Тело запроса:**

​	quality (строка)

​	file (файл)

**Ответ:**

json

```
{
  "id": "uuid",
  "quality": "string",
  "file": "путь",
  "link360": "url",
  "link1080": "url"
}
```

#### 11. GET /api/v1/catalog/videos/{id}/

**Описание:** Детали видео.

**Ответ:** объект видео.

#### 12. DELETE /api/v1/catalog/videos/{id}/

**Описание:** Удаление видео.

#### 13. GET /api/v1/catalog/movies/

**Описание:** Список фильмов с фильтрацией.

Можно производить поиск по полям: точное совпадение по полям director, script_writer, age_restriction, date, date_of_premiere, country, genres (UUID).

**Ответ:**

json

```
[
  { "id": "uuid", "name": "string" }
]
```

#### 14. POST /api/v1/catalog/movies/

**Описание:** Создание нового фильма.

**Тело запроса (JSON):**

	1. name (string) 
	1. description (string)
	1. director (string)
	1. script_writer (string)
	1. age_restriction (string)
	1. date (date)
	1. date_of_premiere (date)
	1. country (string)
	1. subscriptions (список ID подписок)
	1. poster (UUID изображения)
	1. video (UUID видео)
	1. genres (список UUID жанров)

**Ответ:** полный объект фильма  с вложенными жанрами, постером и видео.

#### 15. GET /api/v1/catalog/movies/{id}/

**Описание:** Детальная информация о фильме. При наличии заголовка X-User-Id у запроса регистрируется действие просмотр.

**Ответ:** объект Movie.

#### 16. GET /api/v1/catalog/movies/{id}/genres/

**Описание:** Жанры фильма.

**Ответ:** массив жанров.

#### 17. GET /api/v1/catalog/movies/{id}/film_statistics/

**Описание:** Количество просмотров фильма за период.
**Параметры:** start_timestamp (int), end_timestamp (int)

**Ответ:**

json

```
{ "views_count": 150 }
```

#### 18. GET /api/v1/catalog/movies/top/

**Описание:** Топ фильмов по просмотрам за период.

**Параметры:** start_timestamp, end_timestamp, limit (1-1000)

**Ответ:**

json

```
[
  { "id": "uuid", "name": "string", "views_count": 500 }
]
```

#### 19. GET /api/v1/catalog/movies/subscriptions/{subscription_id}/

**Описание:** Фильмы, доступные по подписке.

**Ответ:** массив фильмов.

#### 20. GET /api/v1/subscriptions/

**Описание:** Список всех доступных подписок.

**Ответ:**

json

```
[
  { "id": 1, "name": "string" }
]
```

#### 21. POST /api/v1/subscriptions/

**Описание:** Создание новой подписки.

**Тело запроса (JSON):**

json

```
{
  "name": "Название",
  "description": "Описание",
  "price": "99.99"
}
```

**Ответ:** полный объект подписки.

#### 22. GET /api/v1/subscriptions/{id}/

**Описание:** Детали подписки.

**Ответ:**

json

```
{
  "id": 1,
  "name": "string",
  "description": "string",
  "price": "decimal"
}
```

#### 23. POST /api/v1/user-subscriptions/add/

**Описание:** Оформление подписки текущему пользователю.

Обязателен заголовок X-User-Id

**Тело запроса:**

json

```
{ "subscription_id": 1 }
```

#### 24. GET /api/v1/user-subscriptions/check/{subscription_id}/

**Описание:** Проверить наличие подписки у текущего пользователя.

Обязателен заголовок X-User-Id

**Ответ:**

json

```
{
  "user_id": "uuid",
  "subscription_id": 1,
  "has_subscription": true
}
```

#### 25. GET /api/v1/user-subscriptions/{subscription_id}/users/

**Описание:** Список пользователей, у которых есть данная подписка.

Обязателен заголовок X-User-Id

**Ответ:**

json

```
{
  "subscription_id": 1,
  "users_count": 2,
  "users": [
    { "user_id": "uuid", "subscription_expires_at": "datetime" }
  ]
}
```

#### 26. GET /api/v1/watchlists

**Описание:** Список watchlist'ов текущего пользователя.

Обязателен заголовок X-User-Id

**Ответ:**

json

```
{
  "count": 5,
  "next": null,
  "previous": null,
  "watchlists": [
    { "id": "uuid", "name": "string" }
  ]
}
```

Поддерживается пагинация.

#### 27. POST /api/v1/watchlists

**Описание:** Создание нового watchlist а.

Обязателен заголовок X-User-Id

**Тело запроса:**

json

```
{ "name": "Мой список" }
```

**Ответ:** полный объект WatchList.

#### 28. GET /api/v1/watchlists/{id}

**Описание:** Детали watchlist'а.

Обязателен заголовок X-User-Id

**Ответ:** WatchList.

#### 29. DELETE /api/v1/watchlists/{id}

**Описание:** Удаление watchlist'а.

#### 30. POST /api/v1/watchlists/{id}/movies

**Описание:** Добавление фильма в watchlist.

Обязателен заголовок X-User-Id

**Тело запроса:**

json

```
{ "movie_id": "uuid фильма" }
```

**Ответ:** обновлённый WatchList.


<pre>
    moiami_resource_service/
    │
    ├── manage.py
    ├── pyproject.toml
    ├── uv.lock
    ├── docker-compose.yaml
    ├── Dockerfile
    ├── Caddyfile
    ├── .dockerignore
    ├── .gitignore
    ├── .python-version
    ├── README.md
    │
    ├── config/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── asgi.py
    │
    ├── apps/
    │   ├── __init__.py
    │   │
    │   ├── actions/
    │   │   ├── __init__.py
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── models.py
    │   │   ├── tests.py
    │   │   └── migrations/
    │   │
    │   ├── catalog/
    │   │   ├── __init__.py
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── models.py
    │   │   ├── tests.py
    │   │   └── migrations/
    │   │
    │   ├── subscription/
    │   │   ├── __init__.py
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── models.py
    │   │   ├── tests.py
    │   │   └── migrations/
    │   │
    │   ├── users/
    │   │   ├── __init__.py
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── models.py
    │   │   ├── tests.py
    │   │   ├── migrations/
    │   │   └── templates/
    │   │       └── registration/
    │   │           └── login.html
    │   │
    │   └── watchlist/
    │       ├── __init__.py
    │       ├── admin.py
    │       ├── apps.py
    │       ├── models.py
    │       ├── tests.py
    │       └── migrations/
    │
    ├── api/
    │   ├── __init__.py
    │   │
    │   ├── common/
    │   │   ├── __init__.py
    │   │   ├── authentication.py
    │   │   ├── permissions.py
    │   │   └── exceptions.py
    │   │
    │   └── v1/
    │       ├── __init__.py
    │       ├── urls.py
    │       │
    │       ├── catalog/
    │       │   ├── __init__.py
    │       │   ├── serializers.py
    │       │   ├── urls.py
    │       │   └── views.py
    │       │
    │       ├── subscription/
    │       │   ├── __init__.py
    │       │   ├── serializers.py
    │       │   ├── urls.py
    │       │   └── views.py
    │       │
    │       ├── users/
    │       │   ├── __init__.py
    │       │   ├── serializers.py
    │       │   ├── urls.py
    │       │   └── views.py
    │       │
    │       └── watchlist/
    │           ├── __init__.py
    │           ├── serializers.py
    │           ├── urls.py
    │           └── views.py
    │
    ├── services/
    │   ├── __init__.py
    │   ├── actions.py
    │   ├── catalog.py
    │   ├── subscriptions.py
    │   ├── users.py
    │   └── watchlist.py
    │
    ├── domain/
    │   ├── __init__.py
    │   ├── exceptions.py
    │   ├── pagination.py
    │   └── errors/
    │       └── __init__.py
    │
    └── docker/
        └── entrypoint.sh
</pre>
