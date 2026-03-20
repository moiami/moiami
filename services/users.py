from django.contrib.auth.models import User
from django.db.models import QuerySet

from apps.subscription.models import UserSubscription
from apps.watchlist.models import WatchList


def get_users() -> QuerySet[User]:
    return User.objects.prefetch_related(
        'profile__watchlists',
        'subscriptions',
    ).all().order_by('date_joined')


def get_subscriptions(user: User) -> QuerySet[UserSubscription]:
    return UserSubscription.objects.filter(user=user)

def get_watchlists(user: User) -> QuerySet[WatchList]:
    return user.profile.watchlists.all()

def create_user(validated_data: dict) -> User:
    return User.objects.create_user(**validated_data)

# TODO: add UserProfile handlers
