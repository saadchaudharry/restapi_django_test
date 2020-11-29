from django.urls import path,include

from .views import CreateUserView,CreateAuthToken,mee
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here


app_name ='user'

urlpatterns = [
    path('create/',CreateUserView,name='create'),
    path('token/',CreateAuthToken.as_view(),name='token'),
    path('update_password/',mee,name='mee'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here

]