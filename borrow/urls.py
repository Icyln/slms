from django.urls import path
from .views import borrow_list, borrow_create, borrow_update, borrow_delete

urlpatterns = [
    path('', borrow_list, name='borrow_list'),
    path('add/', borrow_create, name='borrow_create'),
    path('update/<int:pk>/', borrow_update, name='borrow_update'),
    path('delete/<int:pk>/', borrow_delete, name='borrow_delete'),
]