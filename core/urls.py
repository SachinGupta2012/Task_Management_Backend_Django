"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.http import JsonResponse
from django.conf import settings
from django.utils import timezone


def home(request):
    return JsonResponse({
        "name": "Task Management API",
        "version": "v1",
        "status": "running",
        "environment": "development" if settings.DEBUG else "production",
        "docs": "/api/v1/docs/"
    })


urlpatterns = [
    path('', home),

    path('admin/', admin.site.urls),

    # Versioned API
    path('api/v1/auth/', include('users.urls')),
    path('api/v1/tasks/', include('tasks.urls')),

    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
]

