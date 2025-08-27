from django.urls import path
from .views import DriverStatsView, DriverComparisonsView, analytics_home

urlpatterns = [
    path("", analytics_home, name="analytics-home"),
    path('drivers/<str:full_name>/stats/', DriverStatsView.as_view(), name='driver-stats'),
    path('comparison/', DriverComparisonsView.as_view(), name='driver-comparison')
]