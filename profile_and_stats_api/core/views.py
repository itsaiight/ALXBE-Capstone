from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Team, Driver, Circuit, Race, Result
from .serializers import TeamSerializer, DriverSerializer, CircuitSerializer, RaceSerializer, ResultSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from django_filters import rest_framework
import django_filters

# Create your views here.
def home(request):
    return render(request, 'core/home.html', {
        'user': request.user
    })

class ReadOnlyOrAdminViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get_permissions(self):
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return [AllowAny()]
        return [IsAuthenticated(), IsAdminUser()]

class DriverFilter(django_filters.FilterSet):
    class Meta:
        model = Driver
        fields = {
            'full_name': ['icontains'],
            'debut_year': ['exact', 'gte', 'lte'],
            'current_team__name': ['icontains'],
        }

class TeamViewSet(ReadOnlyOrAdminViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class DriverViewSet(ReadOnlyOrAdminViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    filterset_class = DriverFilter
    filter_backends = [
        rest_framework.DjangoFilterBackend,
        filters.OrderingFilter]

    search_fields = ['full_name', 'current_team__name']
    ordering_fields = ['debut_year', 'number', 'full_name']
    ordering = ['full_name']

class CircuitViewSet(ReadOnlyOrAdminViewSet):
    queryset = Circuit.objects.all()
    serializer_class = CircuitSerializer

class RaceViewSet(ReadOnlyOrAdminViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

class ResultViewSet(ReadOnlyOrAdminViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
