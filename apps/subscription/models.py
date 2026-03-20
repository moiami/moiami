from django.conf import settings
from django.db import models


class Subscription(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ('price',)

    def __str__(self):
        return f"{self.name} (price: {self.price})"


class UserSubscription(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='subscriptions'
    )
    subscription = models.ForeignKey(
        Subscription,
        on_delete=models.PROTECT,
        related_name='user_subscriptions'
    )
    expired_at = models.DateTimeField()

    def __str__(self):
        return f"{self.user.id} - {self.subscription.name}"
