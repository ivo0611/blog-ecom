from django.http import Http404
from django.shortcuts import render, get_object_or_404
from wagtail.admin.widgets import slug
from wagtail.images.models import Image
from wagtail.models import Page
from wagtail.users.forms import User

from .models import BlogCategory, BlogPage


# Create your views here.

# def blog_category(request, category_name):
#     category = BlogCategory.objects.get(name=category_name)
#     posts = category.blog_posts.live()
#     return render(request, "blog/category_list.html", {"category": category, "posts": posts})


def blog_post_view(request, page_id):

    post_data = {
        'ost':123456
    }
    return render(request, "blog_detail.html", post_data)




def home_view(request):
    category_slugs = {
        "bat-tu-menh-ly": "bat_tu_posts",
        "phong-thuy": "phong_thuy_posts",
        "dao-ly-co-nhan": "dao_ly_co_nhan_posts",
        "que-mai-hoa": "que_mai_hoa_posts",
        "vat-pham": "vat_pham_posts",
    }

    context = {var_name: [] for var_name in category_slugs.values()}

    # Lấy ảnh đại diện nếu có
    thumbnail_url = None


    # Lấy bài viết cho từng danh mục
    for slug, var_name in category_slugs.items():
        try:
            category = BlogCategory.objects.get(slug=slug)
            posts = BlogPage.objects.filter(categories=category).order_by('-first_published_at')[:5]

            # Thêm ảnh vào từng bài viết trong context
            for post in posts:
                image_url = post.thumbnail.file.url if post.thumbnail else None
                context[var_name].append({
                    'post': post,
                    'image_url': image_url
                })
        except BlogCategory.DoesNotExist:
            # Bỏ qua nếu danh mục không tồn tại
            continue

    return render(request, 'home/home_page.html', context)


from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import BlogCategory, BlogPage


def category_list(request, slug):
    # Lấy danh mục từ slug
    category = get_object_or_404(BlogCategory, slug=slug)






