from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, DriverViewSet, CircuitViewSet, RaceViewSet, ResultViewSet

router = DefaultRouter()
router.register(r'teams', TeamViewSet, basename='teams')
router.register(r'drivers', DriverViewSet, basename='drivers')
router.register(r'circuits', CircuitViewSet, basename='circuits')
router.register(r'races', RaceViewSet, basename='races')
router.register(r'results', ResultViewSet, basename='results')

urlpatterns = [
    path('', include(router.urls))
]