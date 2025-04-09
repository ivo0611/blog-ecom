from wagtail import hooks
from wagtail.admin.menu import MenuItem
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

@hooks.register('register_admin_menu_item')
def register_blog_menu():
    return MenuItem(_('Bài viết'), reverse('wagtailadmin_explore_root'), icon_name='doc-full')


from wagtail import hooks
from wagtail.admin.viewsets.model import ModelViewSet
from .models import BlogCategory, CategoryListPage


class BlogCategoryViewSet(ModelViewSet):
    model = BlogCategory
    menu_label = "Danh mục bài viết"
    icon = "list-ul"
    add_to_admin_menu = True
    list_display = ["name", "slug"]
    search_fields = ["name"]


    form_fields = ["name", "slug"]
class CategoryListPageViewSet(ModelViewSet):
    model = CategoryListPage
    menu_label = "Trang bài viết theo danh mục"
    icon = "list-ul"
    add_to_admin_menu = True

    form_fields = ["title", "slug","body","category"]



@hooks.register("register_admin_viewset")
def register_blog_category_viewset():
    return BlogCategoryViewSet()


@hooks.register("register_admin_viewset")
def register_category_list_page_viewset():
    return CategoryListPageViewSet()