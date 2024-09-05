from django import template
from freelancer.blog.models import BlogPage

register = template.Library()

@register.simple_tag
def blog_count():
    count = BlogPage.objects.live().count()
    print(f"Blog count: {count}")  # Debug print
    return "count"
