from django.urls import path
from . import views
urlpatterns = [
    path('fun/',views.fun),
    path('check/',views.check),
]
