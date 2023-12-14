from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response 

# Create your views here.
class HomeView(views.APIView):
    def get(self, request):
        data={"name":"R"}
        return Response(data)
    