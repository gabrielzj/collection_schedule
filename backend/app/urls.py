from django.urls import path
from . import views


# TODO: criar rotas para o user
urlpatterns = [
    path('call/create/', views.CollectionCallCreateView.as_view(), name='collection_call_create'),
    path('call/list/', views.CollectionCallListView.as_view(), name='collection_call_list'),
    path('call/<int:pk>/', views.CollectionCallRetrieveView.as_view(), name='collection_call_detail'),
    path('call/delete/<int:pk>/', views.CollectionCallDeleteView.as_view(), name='collection_call_delete'),
]
