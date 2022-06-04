from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import blogDataSerializer, tagSerializer, userSerializer
from .forms import BlogForm
from django.views import View

@api_view(['GET', 'POST'])
def BlogsView(request):
    try: 
        if request.method == 'GET':
            blogs = Blogs.objects.all()
            serializer = blogDataSerializer(blogs,many= "True")
            return Response(serializer.data )
        
        elif request.method == 'POST':
            serializer = blogDataSerializer(data=request.data)
            if serializer.is_valid(raise_exception= True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        return JsonResponse({'error_message': str(e)}, status=500)
        

@api_view(['GET', 'POST'])
def TagsView(request):
    try:
        if request.method == 'GET':
            tags = Tags.objects.all()
            serializer = tagSerializer(tags,many= "True")
            return Response(serializer.data)
        
        elif request.method == 'POST':
            serializer = tagSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        return JsonResponse({'error_message': str(e)}, status=500)
    
@api_view(['GET', 'POST'])
def UserView(request):
    try:
        if request.method == 'GET':
            user = User.objects.all()
            serializer = userSerializer(user,many= "True")
            return Response(serializer.data)
        
        elif request.method == 'POST':
            serializer = userSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return JsonResponse({'error_message': str(e)}, status=500)


def Blog(request):
    try:
        content = Blogs.objects.all()
        info = {'content' : content, "error": False }
        return render(request,"blog.html",info)
    except:
        return HttpResponse("Some error occurred while processing your request")


def Form(request):
    try:
        if request.method == "POST":
            formdata = BlogForm(request.POST, request.FILES)
            if formdata.is_valid():
                formdata.save()
                return redirect("/blog")

        content = BlogForm()
        info = {'content':content}
        return render(request,"add_new.html",info)
    except:
        return HttpResponse("Some error occurred while processing your request")


def View_blog(request,pk):
    try:
        content = Blogs.objects.get(pk= pk)
        info = {'content' : content }
        return render(request,"view_blog.html",info)
    except:
        return HttpResponse("Some error occurred while processing your request")


def Update(request,pk):
    try:
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
    except:
        return HttpResponse("Some error occurred while processing your request")

def Delete(request,pk):
    try:
        particularBlog = Blogs.objects.get(pk= pk)
        particularBlog.delete()
        return redirect("/blog")
    except:
        return HttpResponse("Some error occurred while processing your request")
