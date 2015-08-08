from django.conf.urls import url, include

from rest_framework import routers

from .views import CoachViewSet, PlayerViewSet, TeamViewSet

router = routers.DefaultRouter()
router.register(r'coachs', CoachViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'teams', TeamViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
