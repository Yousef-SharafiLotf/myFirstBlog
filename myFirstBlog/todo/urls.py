from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.sayHello),
    path('all_todos/', views.allTodos),
]