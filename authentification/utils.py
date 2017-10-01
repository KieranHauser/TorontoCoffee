import random
import string

from django.conf import settings


SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 35)


def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
    """Generates random code"""
    return ''.join(random.choice(chars) for _ in range(size))
