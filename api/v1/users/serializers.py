from django.contrib.auth.models import User
from rest_framework import serializers

from apps.subscription.models import UserSubscription
from apps.watchlist.models import WatchList

from services.users import create_user


class UserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubscription
        fields = '__all__'


class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name',
                  'is_staff', 'is_active', 'date_joined']


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

    # By default, serializers have 'create' method, which calls User.objects.create()
    # But it stores plain text
    # So, we override 'create' method for password hashing, which is provided by User.objects.create_user
    def create(self, validated_data):
        """ Called whenever serializer.save() is called  """
        return create_user(validated_data)