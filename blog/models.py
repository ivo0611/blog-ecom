from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from django.db import models
from django_quill.fields import QuillField
from django.utils.text import slugify

class BlogCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class BlogPage(Page):
    intro = models.TextField(blank=True)
    body = QuillField()
    categories = models.ManyToManyField(BlogCategory, blank=True, related_name="blog_posts")

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("body"),
        FieldPanel("categories"),  # ✅ Không cần widget
    ]

    template = "blog/blog_detail.html"
