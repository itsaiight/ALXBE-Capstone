from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Team, Driver, Circuit, Race, Result
from .serializers import TeamSerializer, DriverSerializer, CircuitSerializer, RaceSerializer, ResultSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication

# Create your views here.

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        return Team.objects.all()
    def perform_create(self, serializer):
        serializer.save()  
    def perform_update(self, serializer):
        serializer.save()
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        return Driver.objects.all()
    def perform_create(self, serializer):
        serializer.save()  
    def perform_update(self, serializer):
        serializer.save()
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

class CircuitViewSet(viewsets.ModelViewSet):
    queryset = Circuit.objects.all()
    serializer_class = CircuitSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        return Circuit.objects.all()
    def perform_create(self, serializer):
        serializer.save()  
    def perform_update(self, serializer):
        serializer.save()
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

class RaceViewSet(viewsets.ModelViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        return Race.objects.all()
    def perform_create(self, serializer):
        serializer.save()  
    def perform_update(self, serializer):
        serializer.save()
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        return Result.objects.all()
    def perform_create(self, serializer):
        serializer.save()  
    def perform_update(self, serializer):
        serializer.save()
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)