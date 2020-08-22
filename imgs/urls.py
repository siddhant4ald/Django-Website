from django.urls import path,include
from . import views

urlpatterns = [
    path('imgs/', views.imgs),
    path('imgshow/<int:cid>/',views.imgshow)
]