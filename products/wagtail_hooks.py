from wagtail import hooks
from wagtail.admin.menu import MenuItem
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from wagtail import hooks
from wagtail.admin.viewsets.model import ModelViewSet
from .models import ProductCategory, ProductPage, CategoryProductListPage


class ProductPageViewSet(ModelViewSet):
    model = ProductPage
    menu_label = "Vật phẩm"
    icon = "list-ul"
    add_to_admin_menu = True
    list_display = ["title", "slug","price","purchase_count"]
    search_fields = ["name"]

    form_fields = ["title", "slug","price","purchase_count","body","categories","is_sales","in_stock","thumbnail","sales_price"]





class ProductCategoryViewSet(ModelViewSet):
    model = ProductCategory
    menu_label = "Danh mục vật phẩm"
    icon = "list-ul"
    add_to_admin_menu = True
    list_display = ["name", "slug"]
    search_fields = ["name"]


    form_fields = ["name", "slug"]
# class CategoryListPageViewSet(ModelViewSet):
#     model = CategoryListPage
#     menu_label = "Trang bài viết theo danh mục"
#     icon = "list-ul"
#     add_to_admin_menu = True
#
#     form_fields = ["title", "slug","body","category"]

class CategoryProductListPageViewSet(ModelViewSet):
    model = CategoryProductListPage
    menu_label = "Trang bài viết theo danh mục"
    icon = "list-ul"
    add_to_admin_menu = True

    form_fields = ["title", "slug","body","category"]

@hooks.register("register_admin_viewset")
def register_product_category_viewset():
    return ProductCategoryViewSet()

@hooks.register("register_admin_viewset")
def register_product_page_viewset():
    return ProductPageViewSet()

@hooks.register("register_admin_viewset")
def register_category_product_list_page_viewset():
    return CategoryProductListPageViewSet()