from django import template

register = template.Library()

@register.inclusion_tag('URLshortener/paginator.html')
def paginator(page):
    return {
        'page': page,
    }

@register.inclusion_tag('URLshortener/url_cards.html')
def url_cards(page):
    return {
        'page': page,
    }