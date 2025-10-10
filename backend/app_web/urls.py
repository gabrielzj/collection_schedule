from django.urls import path
from . import views
from .views import CustomTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenVerifyView,
)


urlpatterns = [
    path('auth/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', CustomTokenObtainPairView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('users/', views.register_user, name='user_register'),
    path('calls/', views.list_calls, name='list_calls'),
    path('calls/status/<int:pk>/', views.call_status, name='call_status')
]