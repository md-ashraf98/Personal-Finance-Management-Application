from django.urls import path
from . import views

urlpatterns = [
    path('', views.cover_page, name='cover_page'),
    path('registration/', views.registration, name='registration'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('sign-in/', views.sign_in, name='sign_in'),
    path('home/', views.home, name='home'),
    path('add-transaction/', views.add_transaction, name='add_transaction'),
    path('edit-transaction/<int:pk>/', views.edit_transaction, name='edit_transaction'),
    path('delete-transaction/<int:pk>/', views.delete_transaction, name='delete_transaction'),
]
