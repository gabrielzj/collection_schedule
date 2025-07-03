from django.urls import path
from . import views


# TODO: criar rotas para o user
urlpatterns = [
    path('users/create/', views.UserCreateView.as_view(), name='user_create'),
    path('users/list/', views.UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', views.UserRetrieveView.as_view(), name='user_detail'),
    path('users/update/<int:pk>/', views.UserUpdateView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', views.UserDeleteView.as_view(), name='user_delete'),
    path('call/create/', views.CollectionCallCreateView.as_view(), name='collection_call_create'),
    path('call/list/', views.CollectionCallListView.as_view(), name='collection_call_list'),
    path('call/<int:pk>/', views.CollectionCallRetrieveView.as_view(), name='collection_call_detail'),
    path('call/update/<int:pk>/', views.CollectionCallUpdateView.as_view(), name='collection_call_update'),
    path('call/delete/<int:pk>/', views.CollectionCallDeleteView.as_view(), name='collection_call_delete'),
]
