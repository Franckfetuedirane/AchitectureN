# config/urls.py (modification)
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="API de Gestion Hospitalière",
      default_version='v1',
      description="Documentation de l'API pour le système de gestion hospitalière",
      contact=openapi.Contact(email="contact@hospital.com"),
      license=openapi.License(name="License BSD"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/', include('hospital.api.urls')),
    
    # Documentation
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]