from django.shortcuts import render

from .serilaizer import Userserializer,AuthTokenSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView,permission_classes,authentication_classes
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
# Create your views here.

# class CreateUserView(generics.):
#     serializer_class = Userserializer


@api_view(['POST'])
def CreateUserView(request):
    if request.method=="POST":
        serializer = Userserializer(data=request.data)
        data={}
        if serializer.is_valid():
            User = serializer.save()
            data['email']=User.email
            data['username']=User.username
            data['token']=Token.objects.get(user=User).key
        else:
           data = serializer.errors
        return Response(data)


@api_view(['GET','POST','PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def mee(request):
    if request.method == "GET":
        content = {'message': 'Hello, World!'}
        return Response(content)
    elif request.method == "POST":
        content = {'message': 'form post request'}
        return Response(content)
    elif request.method == "PUT":
        user=request.user
        user.set_password(request.data['password'])
        user.save()
        content = {'message': 'form post put'}
        return Response(content)



# class mee(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [TokenAuthentication]
#
#     def get(self, request):
#         content = {'message': 'Hello, World!'}
#         return Response(content)


class CreateAuthToken(ObtainAuthToken):
    serializer_class = AuthTokenSerializer()
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


