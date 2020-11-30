from .models import Blog
from rest_framework import serializers


class Blogserlizer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields=['title','description','price']