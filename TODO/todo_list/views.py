from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Todo
from django.urls import reverse_lazy

# Create your views here.
class TodoListView(ListView):
    model = Todo
    template_name = 'todo_list/list.html'
    context_object_name = 'todos'
    

class TodoCreateView(CreateView):
    model = Todo
    template_name = 'todo_list/create.html'
    fields = ['title', 'description']
    success_url = reverse_lazy("todo_list")
    

class TodoUpdateView(UpdateView):
    model = Todo
    template_name = 'todo_list/update.html'
    fields = ['title', 'description']    
    success_url = reverse_lazy("todo_list")


class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo_list/delete.html'
    success_url = reverse_lazy("todo_list")



