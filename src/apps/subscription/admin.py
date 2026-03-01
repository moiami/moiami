from django.contrib import admin

from apps.subscription.models import Subscription, UserSubscription


admin.site.register(Subscription)
admin.site.register(UserSubscription)
