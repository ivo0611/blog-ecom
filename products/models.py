import re

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import models
from django_quill.fields import QuillField
from wagtail.admin.panels import FieldPanel
from wagtail.images.widgets import AdminImageChooser
from wagtail.models import Page

def custom_slugify(text):
    """Tạo slug từ text mà không dùng unidecode"""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)  # Loại bỏ ký tự đặc biệt
    text = re.sub(r"\s+", "-", text)  # Thay thế khoảng trắng bằng '-'
    text = re.sub(r"-+", "-", text)  # Xóa gạch ngang thừa
    return text.strip("-")
# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.name)  # Sử dụng custom slugify
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class ProductPage(Page):
    body = QuillField()
    categories = models.ManyToManyField(
        'ProductCategory', blank=True, related_name="product_posts", verbose_name="Danh mục vật phẩm"
    )
    thumbnail = models.ForeignKey(
        "wagtailimages.Image",
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Ảnh đại diện",
    )
    attributes = models.TextField(blank=True)
    # Các trường mới
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Giá", default=0)
    sales_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Giá Giảm", default=0)
    is_sales = models.BooleanField(default=False, verbose_name="Đang khuyến mãi")
    in_stock = models.BooleanField(default=True, verbose_name="Còn hàng")
    purchase_count = models.PositiveIntegerField(default=0, verbose_name="Lượt mua")

    content_panels = Page.content_panels + [
        FieldPanel("body", heading="Mô tả chi tiết sản phẩm"),
        FieldPanel("categories"),
        FieldPanel("attributes", heading="Thuộc tính vật phẩm"),
        FieldPanel("thumbnail", widget=AdminImageChooser()),
        FieldPanel("price"),
        FieldPanel("sales_price"),
        FieldPanel("is_sales"),
        FieldPanel("in_stock"),
        FieldPanel("purchase_count"),

    ]

    template = "product/product_detail.html"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class CategoryProductListPage(Page):
    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE,
        related_name='category_pages',
        verbose_name="Danh mục vật phẩm "
    )
    body = QuillField(blank=True, verbose_name="Mô tả danh mục")

    content_panels = Page.content_panels + [
        FieldPanel('category'),
        FieldPanel("body"),
    ]

    template = "product/product_category_list.html"

    def get_context(self, request):
        context = super().get_context(request)

        # Lấy tất cả sản phẩm nếu title là "all" (không phân biệt hoa thường)
        if self.title == "all":
            posts = ProductPage.objects.live().order_by('-first_published_at')
        else:
            posts = ProductPage.objects.live().filter(
                categories=self.category
            ).order_by('-first_published_at')

        post_list = []
        for post in posts:
            image_url = post.thumbnail.file.url if post.thumbnail else None
            post_list.append({'post': post, 'image_url': image_url})

        paginator = Paginator(post_list, 25)
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
