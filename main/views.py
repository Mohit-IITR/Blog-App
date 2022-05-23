from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import blogDataSerializer, tagSerializer, userSerializer
from .forms import BlogForm
from django.views import View

class BlogsView(viewsets.ModelViewSet):
    queryset = Blogs.objects.all()
    serializer_class = blogDataSerializer

class TagsView(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = tagSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializer

def Blog(request):
    content = Blogs.objects.all()
    info = {'content' : content}
    return render(request,"blog.html",info)

def Form(request):
    if request.method == "POST":
        formdata = BlogForm(request.POST, request.FILES)
        if formdata.is_valid():
            formdata.save()

    formdata = BlogForm()
    content = {'formdata':formdata}
    return render(request,"add_new.html",content)

