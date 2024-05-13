"""
URL configuration for runapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
# from django.urls import path, include, re_path as url
from django.urls import re_path, include, path, re_path

from rest_framework.routers import DefaultRouter
# from core.views import index, RunnersListCreate,RunnersListSet
from core.views import index, runners_list, runners_detail, RegisterView, CreateUserView

router = DefaultRouter()

# router.register(r'runners', RunnersListCreate)
# router.register(r'runset', RunnersListSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/runners/$', runners_list),
    re_path(r'^api/runners/([0-9])$', runners_detail),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('login/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # path('registration/', include('dj_rest_auth.registration.urls')),
    path('registration/',  RegisterView.as_view(), name='rest_register'),
    path('registr/',  CreateUserView.as_view(), name='rester_register'),

    # path("__reload__/", include("django_browser_reload.urls")),
]
