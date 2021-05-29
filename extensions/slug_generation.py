from URLshortener.models import URL
import uuid

def to_base_32(digits):
    decimal = int(digits, 16)
    if decimal < 10:
        return str(decimal)
    else:
        return chr(decimal + 87)

def generate_slug():
    unique_id = uuid.uuid1().hex
    slug = ''.join(to_base_32(unique_id[2*i:2*i+1]) for i in range(8))
    return slug
