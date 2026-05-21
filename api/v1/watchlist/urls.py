from rest_framework.routers import DefaultRouter

from api.v1.watchlist.views import WatchListViewSet

router = DefaultRouter(trailing_slash=False)
router.register("watchlists", WatchListViewSet, basename="watchlist")

urlpatterns = router.urls
