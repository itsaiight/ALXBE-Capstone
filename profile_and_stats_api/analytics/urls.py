from django.urls import path
from .views import DriverStatsView, DriverComparisonsView

urlpatterns = [
    path('drivers/<int:driver_id>/stats/', DriverStatsView.as_view(), name='driver-stats'),
    path('comparison/', DriverComparisonsView.as_view(), name='driver-comparison')
]