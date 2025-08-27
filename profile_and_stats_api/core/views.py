from django.shortcuts import render
from rest_framework import viewsets
from .models import Team, Driver, Circuit, Race, Result
from .serializers import TeamSerializer, DriverSerializer, CircuitSerializer, RaceSerializer, ResultSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

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

class TeamViewSet(ReadOnlyOrAdminViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class DriverViewSet(ReadOnlyOrAdminViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class CircuitViewSet(ReadOnlyOrAdminViewSet):
    queryset = Circuit.objects.all()
    serializer_class = CircuitSerializer

class RaceViewSet(ReadOnlyOrAdminViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

class ResultViewSet(ReadOnlyOrAdminViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
