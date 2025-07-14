from django.urls import path
from . import views

urlpatterns = [
    path('call/list/', views.list_calls, name='list_calls'),
]