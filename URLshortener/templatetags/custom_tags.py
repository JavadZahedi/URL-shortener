from django import template

register = template.Library()

@register.inclusion_tag('URLshortener/paginator.html')
def paginator(page):
    return {
        'page': page,
    }

@register.inclusion_tag('URLshortener/urls_table.html')
def urls_table(page):
    return {
        'page': page,
    }