from django.urls import path
from . import views
from .views import CustomTokenObtainPairView, CustomTokenRefreshView

from rest_framework_simplejwt.views import (
    TokenVerifyView,
)


urlpatterns = [
    path('auth/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('users/', views.register_list_users, name='user_create_list'),
    path('users/<int:pk>/', views.retrieve_update_delete_users, name='user_retrieve_update_delete'),
    path('calls/', views.create_list_collection_call, name='collection_call_create_list'),
    path('calls/<int:pk>/', views.retrieve_update_delete_collection_call, name='collection_call_retrieve_update_delete'),
]
