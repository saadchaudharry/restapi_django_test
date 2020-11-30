from django.urls import path,include
from .views import Blogview
from rest_framework import routers
app_name='blog'

router = routers.DefaultRouter()

router.register(r'blog', Blogview,base_name='Blog')


urlpatterns = [

    # path('blog/',Blogview.as_view(),name='blog'),
    path('',include(router.urls))# <-- And here

]