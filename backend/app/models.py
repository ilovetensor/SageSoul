from django.db import models

# Create your models here.
class DataModel(models.Model):
    Name_of_medicine = models.CharField(max_length = 200, unique = True)
    Reference_name = models.CharField(max_length = 10)
    Dispensing_pack_size = models.CharField(max_length=10)
    Main_indicator = models.TextField()
    Dose = models.TextField()
    Precaution = models.TextField(blank = True)
    Preferred_use = models.CharField(max_length = 10, blank=True)
    Class = models.CharField(max_length=1)

class BookModel(models.Model):
    Book_name = models.CharField(max_length=60)
    Book_content = models.TextField()

    