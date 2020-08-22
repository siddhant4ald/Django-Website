from django.urls import path
from . views import news,bbc
urlpatterns = [
    path('news/', news, name='News'),
    path('bbc/',bbc, name='BBC')

    
]