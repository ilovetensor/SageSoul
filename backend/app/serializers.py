from rest_framework import serializers
from .models import BookModel, DataModel


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = BookModel

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = DataModel