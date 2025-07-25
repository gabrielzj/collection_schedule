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
    path('register/', views.register_user, name='user_register'),
    path('users/list/', views.list_users, name='user_list'),
    path('users/<int:pk>/', views.retrieve_user, name='user_detail'),
    path('users/update/<int:pk>/', views.update_user, name='user_update'),
    path('users/delete/<int:pk>/', views.delete_user, name='user_delete'),
    path('call/create/', views.create_collection_call, name='collection_call_create'),
    path('call/list/', views.list_collection_call, name='collection_call_list'),
    path('call/<int:pk>/', views.retrieve_collection_call, name='collection_call_detail'),
    path('call/update/<int:pk>/', views.update_collection_call, name='collection_call_update'),
    path('call/delete/<int:pk>/', views.delete_collection_call, name='collection_call_delete'),
]
