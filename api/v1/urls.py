from django.urls import include, path

urlpatterns = [
    path('', include('api.v1.subscription.urls')),
    path('', include('api.v1.users.urls')),
    path('', include('api.v1.watchlist.urls')),
    path('catalog/', include('api.v1.catalog.urls')),
]
