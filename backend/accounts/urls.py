from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from rest_framework_simplejwt.views import TokenBlacklistView
from .views import RegistrationView


urlpatterns = [
    path('token/register/', RegistrationView.as_view()),
    path('token/logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('token/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
