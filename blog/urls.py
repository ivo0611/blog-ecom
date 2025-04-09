from django.urls import path

from . import views

urlpatterns = [
path('category/<slug:slug>/', views.category_list, name='category_list'),
path('category/<slug:slug>/', views.category_list, name='category_list'),
]
