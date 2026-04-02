from rest_framework import serializers

from apps.subscription.models import Subscription, UserSubscription


class SubscriptionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ["id", "name"]


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ["id", "name", "description", "price"]
        read_only_fields = ["id"]


class UserSubscriptionSerializer(serializers.ModelSerializer):
    subscription = SubscriptionSerializer(read_only=True)
    user_id = serializers.UUIDField(source='user.id', read_only=True)
    user_name = serializers.CharField(source='user.name', read_only=True)

    class Meta:
        model = UserSubscription
        fields = [
            "id",
            "user_id",
            "user_name",
            "subscription",
            "expired_at",
        ]
        read_only_fields = ["id"]


class SubscribeSerializer(serializers.Serializer):
    subscription_id = serializers.IntegerField()

    def validate_subscription_id(self, value):
        if not Subscription.objects.filter(id=value).exists():
            raise serializers.ValidationError("Subscription not found")
        return value


class UsersWithSubscriptionSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=100)
    subscription_expires_at = serializers.DateTimeField()
