from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(
    r'subscriptions',
    views.SubscriptionViewSet,
    basename='subscription'
)
router.register(
    r'user-subscriptions',
    views.UserSubscriptionViewSet,
    basename='user-subscription'
)

# GET /subscriptions/
# GET /subscriptions/{id}/
# GET /subscriptions/{id}/users/
# GET /user-subscriptions/check/{subscription_id}/
# POST /user-subscriptions/add/

urlpatterns = [
    path('', include(router.urls)),
]
