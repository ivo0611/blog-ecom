from django.urls import path
from .views import blog_category, category_view

urlpatterns = [
    path("category/<str:category_name>/", blog_category, name="blog_category"),
path('category/<slug:category_slug>/', category_view, name='category_view'),
]
