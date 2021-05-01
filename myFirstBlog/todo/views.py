from django.shortcuts import render
from . models import Todo

def sayHello(request):
    return render(request, 'sayHello.html')

def allTodos(request):
    todos = Todo.objects.all()
    context = {'todos': todos, 'pageTitle': 'all todos'}
    return render(request, 'all_todos.html', context)