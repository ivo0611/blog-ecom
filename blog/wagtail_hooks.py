from wagtail import hooks
from wagtail.admin.menu import MenuItem
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

@hooks.register('register_admin_menu_item')
def register_blog_menu():
    return MenuItem(_('Blog'), reverse('wagtailadmin_explore_root'), icon_name='doc-full')


from wagtail import hooks
from wagtail.admin.viewsets.model import ModelViewSet
from .models import BlogCategory


class BlogCategoryViewSet(ModelViewSet):
    model = BlogCategory
    menu_label = "Blog Categories"  # Tên hiển thị trong Admin
    icon = "list-ul"  # Icon trong Admin
    add_to_admin_menu = True  # Hiển thị trên menu chính
    list_display = ["name", "slug"]
    search_fields = ["name"]

    # ✅ Bổ sung form_fields để sửa lỗi
    form_fields = ["name", "slug"]


@hooks.register("register_admin_viewset")
def register_blog_category_viewset():
    return BlogCategoryViewSet()
