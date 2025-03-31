from wagtail import hooks
from wagtail.admin.menu import MenuItem
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

@hooks.register('register_admin_menu_item')
def register_blog_menu():
    return MenuItem(_('Bài viết'), reverse('wagtailadmin_explore_root'), icon_name='doc-full')


from wagtail import hooks
from wagtail.admin.viewsets.model import ModelViewSet
from .models import BlogCategory


class BlogCategoryViewSet(ModelViewSet):
    model = BlogCategory
    menu_label = "Thể loại"
    icon = "list-ul"
    add_to_admin_menu = True
    list_display = ["name", "slug"]
    search_fields = ["name"]


    form_fields = ["name", "slug"]


@hooks.register("register_admin_viewset")
def register_blog_category_viewset():
    return BlogCategoryViewSet()
