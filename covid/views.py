from django.shortcuts import render

from rest_framework.generics import (CreateAPIView,ListCreateAPIView,DestroyAPIView,ListAPIView,UpdateAPIView,RetrieveAPIView,RetrieveUpdateAPIView)

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import generics, status
# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import *

from .models import Profile
from django.core.serializers import serialize


# Create your views here._

class ProfileCreateView(generics.CreateAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    # permission_classes = [permissions.IsAdminUser]
    # required_scopes = ['read:employer']




class ProfileUpdate(APIView):
    def get(self, request, pk, *args, **kwargs):
        print(request, pk)
        print('----++++++++===----------------')
        qs = Profile.objects.get(user=pk)
        print(qs)
        print('--------------------')
        info = serialize('json',[qs,])
        print('--------------------')
        print(info)
        return HttpResponse(info,content_type="application/json")

class ProfileUpdateView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'user-detail'
    # permission_classes = [permissions.IsAdminUser]
    # required_scopes = ['read:employer']

       
	