from django.urls import path
from .import views

urlpatterns = [
    path("",views.index, name="home" ),
    path("test/",views.search, name="search" ),
    path("all/",views.getData, name="getlogs" ),
]