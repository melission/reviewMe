from reviews.models import ReviewBook
from django import template

register = template.Library()

@register.inclusion_tag('reviews_list.html', takes_context=True)
def reviews_list_tag(context):
    print(context)
    pass