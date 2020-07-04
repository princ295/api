"""final_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
    path('api/', include('covid.urls')),
    path('auth/login/', obtain_jwt_token),
    path('auth/refresh-token/', refresh_jwt_token),
    path('auth/signup/', include('rest_auth.registration.urls')),
    path('auth/refresh-token/', refresh_jwt_token),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)