from rest_framework import routers
from django.urls import path, include
from .views import UserViewSet, ActivityViewSet, TeamViewSet, WorkoutViewSet, LeaderboardViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboards', LeaderboardViewSet)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': request.build_absolute_uri('users/'),
        'activities': request.build_absolute_uri('activities/'),
        'teams': request.build_absolute_uri('teams/'),
        'workouts': request.build_absolute_uri('workouts/'),
        'leaderboards': request.build_absolute_uri('leaderboards/'),
    })

urlpatterns = [
    path('', api_root, name='api_root'),
    path('', include(router.urls)),
]
