# fastapi_app/main.py
import os
import django





# Setup Django để sử dụng ORM
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mddq.settings.base")
django.setup()
from fastapi_mddq.routers import blog
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(title="FastAPI for Wagtail Project")

# Optional: Cho phép CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Đăng ký router
app.include_router(blog.router, prefix="/api/blog")
@app.get("/")
def read_root():
    return {"message": "FastAPI is alive!"}