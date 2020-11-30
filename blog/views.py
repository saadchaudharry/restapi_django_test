from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import viewsets

from blog.models import Blog
from blog.serializer import Blogserlizer


class Blogview(viewsets.ModelViewSet):
    serializer_class = Blogserlizer
    queryset = Blog.objects.all()