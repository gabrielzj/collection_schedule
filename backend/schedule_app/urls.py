from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Collection Schedule API",
        default_version='v1',
        description="Documentação da API do projeto Agendamento de Coleta",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="gabrielzuinj@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('app-api/', include('app.urls')),
    path('web-api/', include('app_web.urls')),
]
