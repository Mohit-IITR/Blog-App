from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import blogDataSerializer, tagSerializer, userSerializer
from .forms import BlogForm
from django.views import View

@api_view(['GET', 'POST'])
def BlogsView(request):
    if request.method == 'GET':
        blogs = Blogs.objects.all()
        serializer = blogDataSerializer(blogs,many= "Ture")
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = blogDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def TagsView(request):
    if request.method == 'GET':
        tags = Tags.objects.all()
        serializer = tagSerializer(tags,many= "Ture")
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = tagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def UserView(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = userSerializer(user,many= "Ture")
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def Blog(request):
    content = Blogs.objects.all()
    info = {'content' : content}
    return render(request,"blog.html",info)


def Form(request):
    if request.method == "POST":
        formdata = BlogForm(request.POST, request.FILES)
        if formdata.is_valid():
            formdata.save()
            return redirect("/blog")

    content = BlogForm()
    info = {'content':content}
    return render(request,"add_new.html",info)


def View_blog(request,pk):
    content = Blogs.objects.get(pk= pk)
    info = {'content' : content }
    return render(request,"view_blog.html",info)


def Update(request,pk=0):
    if request.method == "POST":
        particularBlog = Blogs.objects.get(pk= pk)
        update = BlogForm(request.POST, request.FILES ,instance = particularBlog)
        if update.is_valid():
            update.save()
            return redirect("/blog")
        
    particularBlog = Blogs.objects.get(pk= pk)
    content = BlogForm(instance=particularBlog)
    info = {'content':content}
    return render(request,"update.html",info)

def Delete(request,pk):
    particularBlog = Blogs.objects.get(pk= pk)
    particularBlog.delete()
    return redirect("/blog")
