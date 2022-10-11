from django.urls import path
from .views import CreateList, DetailList, TaskList, UpdateList, DeleteList

urlpatterns = [
    path('', TaskList.as_view(), name="tasks"),
    path('task/<int:pk>', DetailList.as_view(), name="detail"),
    path('create-list', CreateList.as_view(), name="create"),
    path('update/<int:pk>', UpdateList.as_view(), name="update"),
    path('delete/<int:pk>', DeleteList.as_view(), name="delete")


    
]