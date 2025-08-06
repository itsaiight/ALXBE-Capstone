from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, DriverViewSet, CircuitViewSet, RaceViewSet, ResultViewSet
from .views import TeamList, DriverList, CircuitList, RaceList, ResultList
from django.contrib.auth import views
router = DefaultRouter()
router.register(r'teams', TeamViewSet, basename='teams')
router.register(r'drivers', DriverViewSet, basename='drivers')
router.register(r'circuits', CircuitViewSet, basename='circuits')
router.register(r'races', RaceViewSet, basename='races')
router.register(r'results', ResultViewSet, basename='results')

urlpatterns = [
    path('teams/', TeamList.as_view(), name='team-list'),
    path('drivers/', DriverList.as_view(), name='driver-list'),
    path('drivers/<int:pk>/', DriverViewSet.get_queryset, name='driver-detail'), #might have to create a driverdetailview
    path('races/', RaceList.as_view(), name='race-list'),
    path('results/', ResultList.as_view(), name='result-list'),
    path('', include(router.urls))
]