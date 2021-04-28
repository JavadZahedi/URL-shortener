from URLshortener.models import URL
import string, random


def generate_slug():
    LETTERS = string.ascii_uppercase + string.ascii_lowercase + string.digits
    slug = ''.join(random.choice(LETTERS) for i in range(8))
    while URL.objects.filter(slug=slug):
        slug = ''.join(random.choice(LETTERS) for i in range(8))
    return slug
