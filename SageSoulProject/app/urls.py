from django.urls import path
from .views import HomePageView, ChatPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('chat/', ChatPageView.as_view(), name='home'),
]