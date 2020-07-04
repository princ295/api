from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('p/', views.ProfileCreateView.as_view()),
    path('p/<int:pk>/',views.ProfileUpdateView.as_view()),
    # path('i/', views.ProfileUpdate.as_view()),
    path('i/<int:pk>/',views.ProfileUpdate.as_view()),
]
