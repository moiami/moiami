from django.urls import path

from api.v1.catalog import views as catalog_views

urlpatterns = [
    path("catalog/views/", catalog_views.vote, name="catalog-views"),
]
