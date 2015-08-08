from django.conf.urls import url, include

from rest_framework import routers

from .views import ParticipantViewSet, TournamentViewSet

router = routers.DefaultRouter()
router.register(r'participant', ParticipantViewSet)
router.register(r'tournaments', TournamentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
