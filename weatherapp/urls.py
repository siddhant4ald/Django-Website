from django.urls import path
from . import views
urlpatterns = [
    path('report/',views.report,name="wet"),
    path('delete/<city_name>/',views.delete_city,name='delete_city')
]
