from django.contrib import admin

from apps.catalog.models import Genre, Image, Movie, Video

admin.site.register(Genre)
admin.site.register(Video)
admin.site.register(Image)
admin.site.register(Movie)
