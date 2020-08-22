from django.urls import path
from . import views

urlpatterns = [
    path('diary/', views.diary),
    path('add/', views.add, name='add'),
    path('deldiary/',views.deldiary)
]