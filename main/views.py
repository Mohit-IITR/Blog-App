from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import blogDataSerializer, tagSerializer, userSerializer

class BlogsView(viewsets.ModelViewSet):
    queryset = Blogs.objects.all()
    serializer_class = blogDataSerializer

class TagsView(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = tagSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializer