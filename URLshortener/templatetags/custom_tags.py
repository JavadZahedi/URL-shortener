from django import template

register = template.Library()

@register.inclusion_tag('URLshortener/paginator.html', takes_context=True)
def paginator(context, page):
    return {
        'request': context['request'],
        'page': page,
    }

@register.inclusion_tag('URLshortener/url_cards.html', takes_context=True)
def url_cards(context, page):
    return {
        'request': context['request'],
        'page': page,
    }

@register.inclusion_tag('URLshortener/search_field.html', takes_context=True)
def search_field(context, search_page):
    return {
        'request': context['request'],
        'search_page': search_page,
    }

@register.simple_tag
def about_us_text():
    return 'این وب سایت برای کوتاه کردن لینک های بلند طراحی شده است و شما \
    می توانید با ثبت نام در این سایت به تعداد دلخواه لینک مورد نظر خود را وارد \
    و کوتاه کنید.'