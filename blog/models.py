import re

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from django.db import models
from django_quill.fields import QuillField
from wagtail.images.widgets import AdminImageChooser
from django.utils.text import slugify
from django.shortcuts import get_object_or_404, render
# ✅ Định nghĩa hàm tạo slug bên ngoài class
def custom_slugify(text):
    """Tạo slug từ text mà không dùng unidecode"""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)  # Loại bỏ ký tự đặc biệt
    text = re.sub(r"\s+", "-", text)  # Thay thế khoảng trắng bằng '-'
    text = re.sub(r"-+", "-", text)  # Xóa gạch ngang thừa
    return text.strip("-")

class BlogCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.name)  # Sử dụng custom slugify
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class BlogPage(Page):
    intro = models.TextField(blank=True, verbose_name="Giới thiệu")
    body = QuillField()
    categories = models.ManyToManyField(
        BlogCategory, blank=True, related_name="blog_posts", verbose_name="Danh mục bài viết"
    )
    thumbnail = models.ForeignKey(
        "wagtailimages.Image",
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Ảnh đại diện",
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        FieldPanel("categories"),
        FieldPanel("thumbnail", widget=AdminImageChooser()),
    ]

    template = "blog/blog_detail.html"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class CategoryListPage(Page):
    category = models.ForeignKey(
        BlogCategory, on_delete=models.CASCADE,
        related_name='category_pages',
        verbose_name="Danh mục"
    )
    body = QuillField(blank=True, verbose_name="Mô tả danh mục")

    content_panels = Page.content_panels + [
        FieldPanel('category'),
        FieldPanel("body"),
    ]

    template = "blog/category_list.html"

    def get_context(self, request):
        context = super().get_context(request)

        # Lấy tất cả bài viết thuộc category
        posts = BlogPage.objects.live().filter(categories=self.category).order_by('-first_published_at')

        post_list = []
        for post in posts:
            image_url = post.thumbnail.file.url if post.thumbnail else None
            post_list.append({'post': post, 'image_url': image_url})


        paginator = Paginator(post_list, 5)
        page = request.GET.get('page')

        try:
            paginated_posts = paginator.page(page)
        except PageNotAnInteger:
            paginated_posts = paginator.page(1)
        except EmptyPage:
            paginated_posts = paginator.page(paginator.num_pages)

        context['category'] = self.category
        context['posts'] = paginated_posts  # dùng trong template
        return context
