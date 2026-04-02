from django.contrib.auth.models import User
from django.db.models import QuerySet


def get_users() -> QuerySet[User]:
    return User.objects.prefetch_related(
        'subscriptions',
    ).all().order_by('date_joined')

def create_user(validated_data: dict) -> User:
    return User.objects.create_user(**validated_data)

# TODO: add UserProfile handlers
