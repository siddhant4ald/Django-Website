from django.urls import path
from . import views

urlpatterns =[
    path('index1/', views.index1, name="index1"),
    path('updateTask/<int:pk>/', views.updateTask, name="updateTask"),
    path('deleteTask/<int:pk>/', views.deleteTask, name="deleteTask"),
]




'''from django.urls import path
from . import views
urlpatterns = [
    path('note/',views.note),
    path('add/',views.add),
    path('deleteItem/<int:todo_id>/',views.deleteItem),
]
'''