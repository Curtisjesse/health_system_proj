from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from drf_spectacular.views import (
    SpectacularAPIView, 
    SpectacularSwaggerView,
    SpectacularRedocView
)

urlpatterns = [
    # Redirect root URL to API docs
    path('', RedirectView.as_view(url='/api/docs/', permanent=False), name='index'),
    
    path('admin/', admin.site.urls),
    path('api/', include('health_core.urls')),
    path('api-auth/', include('rest_framework.urls')),
    
    # API Schema and documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]