from django.db import models

# Create your models here.
class DataModel(models.Model):
    herb = models.CharField(max_length=100)
    name = models.TextField(blank=True)
    hindi_name = models.TextField(blank=True)
    english_name = models.TextField(blank=True)
    properties_rasa = models.TextField()
    properties_guna = models.TextField()
    properties_virya = models.TextField()
    properties_vipaka = models.TextField()
    effects_on_dosa = models.TextField()
    caution = models.TextField(blank=True)

