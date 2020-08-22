"""db3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',views.index),
    path('index/',views.index),
    path('insert/',views.insert),
    path('search/',views.search),
    path('show/',views.show),
    path('delete/',views.delete),
    path('update/',views.update),
    path('updel/',views.updel),
    path('edit/',views.edit),
    path('updateres/',views.updateres),
    path('about/',views.about),
    path('',include('weatherapp.urls')),
    path('',include('news.urls')),
    path('',include('game.urls')),
    path('',include('todo.urls')),
    path('',include('register.urls')),
    path('',include("django.contrib.auth.urls")),
    path('',include('diary.urls')),
    path('',include("imgs.urls")),
    #path('imgshow/<int:cid>/',views.imgshow),
    #path('imgshow/<int:cid>/',include("imgs.urls"))

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


