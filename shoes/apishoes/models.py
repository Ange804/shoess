from django.db import models

class chauss(models.Model):
    name = models.CharField(max_length=100)
    prix = models.FloatField()
    quantite = models.IntegerField()
    image = models.CharField(max_length=25096)


