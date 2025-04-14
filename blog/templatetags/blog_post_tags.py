from django import template

from blog.models import BlogPage

from blog.models import BlogCategory

register = template.Library()


@register.inclusion_tag('blog/partials/sidebar.html')
def render_sidebar():
    posts = BlogPage.objects.live().order_by('-first_published_at')[:5]
    return {'latest_posts': posts}



@register.inclusion_tag('blog/partials/related_post.html', takes_context=True)
def render_related_posts(context):
    related_posts = []
    try:
        current_page = context.get('page')

        if isinstance(current_page, BlogPage):
            # Giả sử mỗi bài có ít nhất 1 category
            categories = current_page.categories.all()

            if categories.exists():
                # Lấy category đầu tiên (hoặc bạn có thể lấy theo tiêu chí riêng)
                category = categories.first()

                related_posts = (
                    BlogPage.objects.live()
                    .filter(categories=category)
                    .exclude(id=current_page.id)
                    .order_by('-first_published_at')[:5]
                )
    except Exception as e:
        # Có thể log lỗi nếu cần
        pass

    return {'related_posts': related_posts}
