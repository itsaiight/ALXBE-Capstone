from rest_framework import serializers
from .models import Team, Driver, Circuit, Race, Result

class TeamSerializer(serializers.Serializer):
    class Meta:
        model = Team
        fields = ['team_id', 'name', 'country']

class DriverSerializer(serializers.Serializer):
    current_team = TeamSerializer(read_only=True)
    class Meta:
        model = Driver
        fields = ['driver_id', 'full_name', 'number', 'nationality', 'debut_year', 'current_team', 'stats', 'image_url']

class CircuitSerializer(serializers.Serializer):
    class Meta:
        model = Circuit
        fields = ['circuit_id', 'name', 'location', 'length_km']

class RaceSerializer(serializers.Serializer):
    circuit = CircuitSerializer(read_only=True)
    class Meta:
        model = Race
        fields = ['race_id', 'name', 'round_number', 'year', 'circuit', 'date']

class ResultSerializer(serializers.Serializer):
    driver = DriverSerializer(read_only=True)
    race = RaceSerializer(read_only=True)
    class Meta:
        model = Result
        fields = ['result_id', 'driver', 'race', 'position', 'points']