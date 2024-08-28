from django import template
from freelancer.base.models import FooterContent

register = template.Library()

@register.simple_tag
def get_footer_content():
    """
    Retrieves the first instance of FooterContent.
    """
    return FooterContent.objects.first()
