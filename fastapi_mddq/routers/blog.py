# fastapi_app/routers/blog.py
from fastapi import APIRouter
from django.apps import apps

Page = apps.get_model('blog', 'BlogPage')  # Tên app và model bạn đang dùng

router = APIRouter()

@router.get("/")
def list_page():
    queryset = Page.objects.all().values("id", "title","categories","body")[:50]
    return list(queryset)