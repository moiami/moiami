from rest_framework import serializers

from apps.catalog.models import Genre, Image, Movie, Video


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]
        read_only_fields = ["id"]

class ImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["id", "link"]

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["id", "link"]
        read_only_fields = ["id"]

class VideoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ["id", "link360","link1080"]

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ["id","link360","link1080"]
        read_only_fields = ["id"]

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "name"]

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreListSerializer(many=True, read_only=True)
    poster = ImageListSerializer(read_only=True)
    video = VideoListSerializer(read_only=True)
    class Meta:
        model = Movie
        fields = ['id','name','description','director','script_writer','age_restriction','date','date_of_premiere','country','genres','subscriptions','poster','video',]
        read_only_fields = ["id"]


class MovieStatisticsQuerySerializer(serializers.Serializer):
    start_timestamp = serializers.DateTimeField()
    end_timestamp = serializers.DateTimeField()

    def validate(self, attrs):
        if attrs['start_timestamp'] > attrs['end_timestamp']:
            raise serializers.ValidationError(
                'start_timestamp must be less than or equal to end_timestamp'
            )

        return attrs


class GenreMovieSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(read_only=True)
    genre_id = serializers.UUIDField(source='genre.id', read_only=True)
    genre_name = serializers.CharField(source='genre.name', read_only=True)
    class Meta:
        model = Genre
        fields = ["id","name"]
        read_only_fields = ["id"]
