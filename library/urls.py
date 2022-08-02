"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from books.views import BooksViewSet

router = DefaultRouter()
router.register('books', BooksViewSet, basename='Books')

urlpatterns = [
    path('users/', include('users.urls')),
    path('', include(router.urls)),
    path('swagger/schema/', SpectacularAPIView.as_view(), name='swagger-schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='swagger-schema'), name='swagger-ui'),
]
