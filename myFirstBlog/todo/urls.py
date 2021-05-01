from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.sayHello, name='hello'),
    path('all_todos/', views.allTodos, name='alltodos'),
    path('<int:id>/', views.detail, name='detail'),
]