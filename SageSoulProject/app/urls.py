from django.urls import path
from .views import HomePageView, ChatPageView, getAnswerView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('chat/', ChatPageView.as_view(), name='home'),
    path('getAnswer/', getAnswerView.as_view(), name='answer'),
]