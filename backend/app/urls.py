from django.urls import path
from .views import HomeView, similarityView, chatView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('similarity/', similarityView.as_view(), name='similarity'),
    path('chat/', chatView.as_view(), name='similarity'),
]