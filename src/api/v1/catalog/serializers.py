from rest_framework import serializers

from apps.catalog.models import Movie,Image,Genre,Video

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
    class Meta:
        model = Movie
        fields = ["id", "name","description","director","script_writer","age_restriction","date","date_of_premiere","country","poster_id","video_id"]
        read_only_fields = ["id"]

class GenreMovieSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(read_only=True)
    genre_id = serializers.UUIDField(source='genre.id', read_only=True)
    genre_name = serializers.CharField(source='genre.name', read_only=True)
    class Meta:
        model = Genre
        fields = ["id","name"]
        read_only_fields = ["id"]

#class SubscriptionListSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Subscription
#        fields = ["id", "name"]
#

#class SubscriptionSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Subscription
#        fields = ["id", "name", "description", "price"]
#        read_only_fields = ["id"]


#class UserSubscriptionSerializer(serializers.ModelSerializer):
#    subscription = SubscriptionSerializer(read_only=True)
#    user_id = serializers.UUIDField(source='user.id', read_only=True)
#    user_name = serializers.CharField(source='user.name', read_only=True)

#    class Meta:
#        model = UserSubscription
#        fields = [
#            "id",
#            "user_id",
#            "user_name",
#            "subscription",
#            "expired_at",
#        ]
#        read_only_fields = ["id"]


#class SubscribeSerializer(serializers.Serializer):
#    subscription_id = serializers.IntegerField()

#    def validate_subscription_id(self, value):
#        try:
#            subscription = Subscription.objects.get(id=value)

#        except Subscription.DoesNotExist:
#            raise serializers.ValidationError("Subscription not found")

#        return subscription


#class UsersWithSubscriptionSerializer(serializers.Serializer):
#    id = serializers.UUIDField()
#    name = serializers.CharField()
#    is_admin = serializers.BooleanField()
#    subscription_expires_at = serializers.DateTimeField()