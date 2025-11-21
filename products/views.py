from django.shortcuts import render
from wagtail.models import Page

from mddq.products.models import ProductPage, ProductCategory


# Create your views here.
# models.py
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import ProductCategory, ProductPage


def category_list(request, slug):
    # Lấy danh mục từ slug
    category = get_object_or_404(ProductCategory, slug=slug)