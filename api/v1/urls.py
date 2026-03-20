from django.urls import path, include

urlpatterns = [
    # path('', include('api.v1.subscription.urls')),
    path('', include('api.v1.users.urls')),
    # path('', include('api.v1.catalog.urls')),
    # path('', include('api.v1.watchlist.urls')),
]