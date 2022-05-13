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

def Blog(request):
    return render(request,"blog.html")

def Form(request):
    
    if request.method == 'POST':
        user = request.POST.get('author')
        title= request.POST.get('title')
        tag_data= request.POST.get('tag')
        small_desc= request.POST.get('small-desc')
        full_content= request.POST.get('full-content')
        image= request.POST.get('image')
        # formdata = Blogs(title=title, tag=tag,small_dec=small_desc, full_content= full_content, img = image)
        author = User.objects.create(name = user)
        blogdata = Blogs.objects.create(author = author,title=title,small_desc=small_desc, full_content= full_content, img = image)
        tagdata = Tags.objects.create(tags = tag_data)

        blogdata.tag.add(tagdata)
    return render(request,"add_new.html")