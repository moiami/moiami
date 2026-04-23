# Resource service

#### Сервис ресурсов команды moiami написанный на django.

##### Сущьности сервиса:

​	Action

​	ActionType

​	Genre

​	Video

​	Image

​	Movie

​	Subscription

​	UserSubscription

​	User

​	Watchlist

### Эндпоинты:

1. GET /api/v1/catalog/movies/ 
2. GET /api/v1/catalog/movies/{id}/
3. GET /api/v1/catalog/movies/{id}/genres/
4. GET /api/v1/catalog/movies/subscriptions/{subscription_id}/
5. GET /api/v1/catalog/genres/
6. GET /api/v1/catalog/genres/{id}/
7.  GET /api/v1/catalog/images/ 
8.  GET /api/v1/catalog/images/{id}/
9. GET /api/v1/catalog/videos/ 
10. GET /api/v1/catalog/videos/{id}/ 
11. GET /api/v1/subscriptions/
12. GET /api/v1/subscriptions/{id}/
13. POST /api/v1/user-subscriptions/add/ 
14. GET /api/v1/user-subscriptions/check/{subscription_id}/ 
15. GET /api/v1/user-subscriptions/{subscription_id}/users/
16. POST /api/v1/users/
17. GET /api/v1/users/
18. GET /api/v1/users/{id}/ 
19. GET /api/v1/users/{id}/subscriptions/
20. GET /api/v1/users/{id}/watchlists/
21. GET /api/v1/watchlists 
22. POST /api/v1/watchlists 
23. GET /api/v1/watchlists/{id}
24. PUT /api/v1/watchlists/{id} 
25. PATCH /api/v1/watchlists/{id}
26. DELETE /api/v1/watchlists/{id} 
27. POST /api/v1/watchlists/{id}/movies

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