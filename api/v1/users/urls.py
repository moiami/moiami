from rest_framework.routers import DefaultRouter

from api.v1.users.views import UserViewSet

app_name = "api_v1_users"

router = DefaultRouter()
router.register("users", UserViewSet, basename="user")

urlpatterns = router.urls
