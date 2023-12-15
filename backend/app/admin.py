from django.contrib import admin
from .models import DataModel, BookModel

# Register your models here.
admin.site.register(DataModel)
admin.site.register(BookModel)