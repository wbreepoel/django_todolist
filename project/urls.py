"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from register import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")), 
    path('register/', v.register, name='register'),
     path('', include('django.contrib.auth.urls')),  
# So if we don't type admin/, whatever the path is given is going to be passed over to the urls.py file in the main folder
]

# The URLS here define what's going to happen when we go to a certain link 
# what page we are going to direct into
# The URLS given is going to passed over to the urls.py file in the main folder
# what include does: it looks for a path of whatever is specified in the string before. So first case it's /admin and second case it's nothing
# we then take everything after that path and send it to the urls.py in the main folder
# for example if the path is as follows /home/start and the path statement is like this path('home/',include('main.urls'))
# we are going to look for the home/ path, if we find it we pass start (which is left from the path) over to the main url file
# The main urls is going to look for a path that is called start. If it does it going to direct us to the function that we
# defined in the views.py file