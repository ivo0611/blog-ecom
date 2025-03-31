from django.shortcuts import render, get_object_or_404
from wagtail.models import Page
from wagtail.users.forms import User

from .models import BlogCategory, BlogPage


# Create your views here.

# def blog_category(request, category_name):
#     category = BlogCategory.objects.get(name=category_name)
#     posts = category.blog_posts.live()
#     return render(request, "blog/category_list.html", {"category": category, "posts": posts})


def blog_post_view(request, page_id):
    page = Page.objects.get(id=page_id).specific
    owner = User.objects.get(id=page.owner_id)  # Lấy thông tin chủ sở hữu

    return render(request, "blog_detail.html", {
        "page": page,
        "owner_name": owner.get_full_name() or owner.username,  # Sử dụng tên đầy đủ nếu có
    })


def category_view(request, category_slug):
    category = get_object_or_404(BlogCategory, slug=category_slug)
    posts = BlogPage.objects.filter(categories__in=[category]).live().order_by('-first_published_at')

    return render(request, "blog/category_list.html", {
        "category": category,
        "posts": posts
    })