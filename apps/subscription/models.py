from django.db import models


class Subscription(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ("price",)

    def __str__(self):
        return f"{self.name} (price: {self.price})"


class UserSubscription(models.Model):
    user_id = models.UUIDField(db_index=True)
    subscription = models.ForeignKey(
        Subscription,
        on_delete=models.PROTECT,
        related_name="user_subscriptions",
    )
    expired_at = models.DateTimeField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user_id", "subscription"],
                name="unique_user_subscription",
            )
        ]

    def __str__(self):
        return f"{self.user_id} - {self.subscription.name}"
