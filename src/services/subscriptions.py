from django.db.models import QuerySet
from django.utils import timezone

from apps.subscription.models import Subscription, UserSubscription
from domain.exceptions import SubscriptionNotFound


def get_subscription(subscription_id: int) -> Subscription:
    try:
        return Subscription.objects.get(id=subscription_id)
    except Subscription.DoesNotExist as e:
        raise SubscriptionNotFound(
            f"Subscription with id={subscription_id} does not exist."
        ) from e


def get_available_subscriptions() -> QuerySet[Subscription]:
    return Subscription.objects.all()


def get_user_subscriptions(user_id: int) -> QuerySet[UserSubscription]:
    return (
        UserSubscription.objects
        .select_related("subscription", "user")
        .filter(user_id=user_id)
        .order_by("expired_at")
    )


def subscribe_user(user_id: int, subscription_id: int | Subscription) -> UserSubscription:
    pass


def check_subscription(user_id: int, subscription_id: int) -> bool:
    get_subscription(subscription_id)

    return UserSubscription.objects.filter(
        user_id=user_id,
        subscription_id=subscription_id,
        expired_at__gt=timezone.now(),
    ).exists()


def get_users_with_subscription(subscription_id: int):
    pass
