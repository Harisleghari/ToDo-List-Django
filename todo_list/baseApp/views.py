from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Task


class CustomLogin(LoginView):
    template_name = 'base/loginpage.html'
    fields = '__all__'
    redirect_authenticated_user: True

    def get_success_url(self):
        return reverse_lazy('tasks')


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'base/task_list.html'
    context_object_name = 'tasks'


class DetailList(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'base/task_detail.html'
    context_object_name = 'tasks'


class CreateList(LoginRequiredMixin, CreateView):
    model = Task
    fields = '__all__'
    template_name = 'base/task_create.html'
    success_url = reverse_lazy('tasks')


class UpdateList(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'base/task_create.html'
    success_url = reverse_lazy('tasks')


class DeleteList(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task_delete.html'
    success_url = reverse_lazy('tasks')