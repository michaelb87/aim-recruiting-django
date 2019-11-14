from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=50)

class Source(models.Model):
    name = models.CharField(max_length=100)

class RevenueRecord(models.Model):
    date = models.DateField()
    publisher = models.ForeignKey(Publisher)
    source = models.ForeignKey(Source)
    clicks = models.IntegerField()
    revenue = models.FloatField()
