from django.contrib.auth.models import User
from django.db.models import QuerySet


def get_users() -> QuerySet[User]:
    return User.objects.all().order_by("date_joined")


def create_user(validated_data: dict) -> User:
    return User.objects.create_user(**validated_data)
