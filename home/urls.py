from django.urls import path
from . import views
from blog.views import home_view

urlpatterns = [
    path('', home_view, name='home'),

]