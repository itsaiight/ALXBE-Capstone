from django.db import models

# Create your models here.
class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=250)
    number = models.IntegerField()
    nationality = models.CharField(max_length=100)
    debut_year = models.IntegerField()
    current_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    stats = models.JSONField(null=True, blank=True) #might change this to a JSONField or similar for complex stats 
    image_url = models.URLField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return self.full_name
    
class Circuit(models.Model):
    circuit_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    length_km = models.FloatField()

    def __str__(self):
        return self.name
    
class Race(models.Model):
    race_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    round_number = models.IntegerField()
    year = models.IntegerField()
    circuit = models.ForeignKey(Circuit, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.year})"
    
class Result(models.Model):
    result_id = models.AutoField(primary_key=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    position = models.IntegerField()
    points = models.FloatField()

    def __str__(self):
        return f"{self.driver.full_name} - {self.position} at {self.race.name}"
    
