from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='index'),
    path("<int:id>", views.todo, name='todo'),
    path("create/", views.create, name='create'),
    path("organize/", views.organize, name='organize'),
 
]

# if we typed nothing we will be directed to the home page
# if we typed an integer it will direct us to the todo page
# These views are connected to the views.py file
# 