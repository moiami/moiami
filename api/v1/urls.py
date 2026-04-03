from django.urls import include, path

urlpatterns = [
    path('subscriptions/', include('api.v1.subscription.urls')),
    path('users/', include('api.v1.users.urls')),
    path('watchlists/', include('api.v1.watchlist.urls')),
    path('catalog/', include('api.v1.catalog.urls')),
]
