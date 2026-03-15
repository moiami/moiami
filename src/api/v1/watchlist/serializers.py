from rest_framework import serializers

from apps.catalog.models import Movie
from apps.watchlist.models import WatchList


class WatchListMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name']
        read_only_fields = ['id', 'name']


class WatchListListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        trim_whitespace=True
    )

    class Meta:
        model = WatchList
        fields = ['id', 'name']
        read_only_fields = ['id']


class WatchListSerializer(WatchListListSerializer):
    movies = WatchListMovieSerializer(many=True, read_only=True)

    class Meta(WatchListListSerializer.Meta):
        fields = ['id', 'name', 'movies']
        read_only_fields = ['id', 'movies']
