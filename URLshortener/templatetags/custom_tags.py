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

@register.simple_tag
def about_us_text():
    return 'این وب سایت برای کوتاه کردن لینک های بلند طراحی شده است و شما \
    می توانید با ثبت نام در این سایت به تعداد دلخواه لینک مورد نظر خود را وارد \
    و کوتاه کنید.'