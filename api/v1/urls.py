from django.urls import path, include

from api.v1.catalog import views as catalog_views

urlpatterns = [
    path('catalog/', include('api.v1.catalog.urls')),
]
