from django.contrib import admin

from wagtail.snippets.models import register_snippet
from django.db import models
from .models import BlogCategory



from wagtail import hooks
from wagtail.admin.viewsets.model import ModelViewSet
from .models import BlogCategory
#
# class BlogCategoryViewSet(ModelViewSet):
#     model = BlogCategory
#     menu_label = "Blog Categories"  # Tên hiển thị trên admin
#     icon = "list-ul"  # Icon trong admin
#     add_to_admin_menu = True  # Hiển thị trên menu chính
#     list_display = ["name", "slug"]
#     search_fields = ["name"]
#     form_fields = ['name']
#
# @hooks.register("register_admin_viewset")
# def register_blog_category_viewset():
#     return BlogCategoryViewSet()