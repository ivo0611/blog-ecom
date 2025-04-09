from django import template

from blog.models import BlogPage

register = template.Library()


@register.inclusion_tag('blog/partials/sidebar.html')
def render_sidebar():
    posts = BlogPage.objects.live().order_by('-first_published_at')[:5]
    return {'latest_posts': posts}