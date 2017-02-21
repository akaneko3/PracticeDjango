from django.db import models

# Create your models here.


class District(models.Model):
    name = models.CharField(max_length=30)


class Prefecture(models.Model):
    name = models.CharField(max_length=30)
    district = models.ForeignKey(District, on_delete=models.CASCADE)


class City(models.Model):
    name = models.CharField(max_length=30)
    prefecture = models.ForeignKey(Prefecture, on_delete=models.CASCADE)
    designated = models.DateField()
    area = models.DecimalField(max_digits=7, decimal_places=2)
    population = models.IntegerField()
