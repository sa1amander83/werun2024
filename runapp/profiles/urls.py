from django.urls import  include, path, re_path

from .views import  profile
urlpatterns = [

    path('<str:username>/', profile, name="profile"),


]
