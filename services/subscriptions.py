from datetime import timedelta
from typing import Any
from uuid import UUID

from django.db import transaction
from django.db.models import QuerySet
from django.utils import timezone

from apps.subscription.models import Subscription, UserSubscription
from domain.exceptions import SubscriptionNotFound

SUBSCRIPTION_DURATION_DAYS = 30


def get_subscription(subscription_id: int) -> Subscription:
    subscription = Subscription.objects.filter(id=subscription_id).first()
    if not subscription:
        raise SubscriptionNotFound(
            f"Subscription with id={subscription_id} does not exist"
        )
    return subscription


def get_available_subscriptions() -> QuerySet[Subscription]:
    return Subscription.objects.all()


def get_user_subscriptions(user_id: UUID) -> QuerySet[UserSubscription]:
    return (
        UserSubscription.objects
        .select_related("subscription")
        .filter(user_id=user_id)
        .order_by("expired_at")
    )


@transaction.atomic
def subscribe_user(user_id: UUID, subscription_id: int) -> UserSubscription:
    now = timezone.now()
    subscription = (
        subscription_id
        if isinstance(subscription_id, Subscription)
        else get_subscription(subscription_id)
    )

    user_subscription, created = (
        UserSubscription.objects
        .select_for_update()
        .get_or_create(
            user_id=user_id,
            subscription=subscription,
            defaults={
                "expired_at": now + timedelta(days=SUBSCRIPTION_DURATION_DAYS)
            }
        )
    )

    if not created:
        start_time = max(user_subscription.expired_at, now)
        user_subscription.expired_at = start_time + \
            timedelta(days=SUBSCRIPTION_DURATION_DAYS)
        user_subscription.save(update_fields=["expired_at"])

    return user_subscription


def check_subscription(user_id: UUID, subscription_id: int) -> bool:
    get_subscription(subscription_id)

    return UserSubscription.objects.filter(
        user_id=user_id,
        subscription_id=subscription_id,
        expired_at__gt=timezone.now(),
    ).exists()


def get_users_with_subscription(subscription_id: int) -> list[dict[str, Any]]:
    get_subscription(subscription_id)

    user_subscriptions = (
        UserSubscription.objects
        .filter(subscription_id=subscription_id)
        .order_by("expired_at")
    )

    return [_map_user_subscription(item) for item in user_subscriptions]


def _map_user_subscription(user_subscription: UserSubscription) -> dict[str, Any]:
    return {
        "user_id": user_subscription.user_id,
        "subscription_expires_at": user_subscription.expired_at,
    }
