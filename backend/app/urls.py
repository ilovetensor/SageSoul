from django.urls import path
from .views import similarityView, chatView

urlpatterns = [
    path('similarity/', similarityView.as_view(), name='similarity'),
    path('chat/', chatView.as_view(), name='similarity'),
]