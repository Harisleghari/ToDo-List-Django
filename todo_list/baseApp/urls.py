from django.urls import path
from .views import DetailList, TaskList, DetailView

urlpatterns = [
    path('', TaskList.as_view(), name="tasks"),
    path('task/<int:pk>', DetailList.as_view(), name="detail")
    
]