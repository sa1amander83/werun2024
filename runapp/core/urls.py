from django.urls import path, include

from core.views import index,  RunnersListCreate

urlpatterns = [

    path('', index),
    # path('api/home/', RunnersListCreate.as_view()),
    # path('api/home/', apindex),


    # path("__reload__/", include("django_browser_reload.urls")),

]
