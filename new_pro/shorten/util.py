import random
from .models import bitly

def code_gen():
    shrt = ''
    for i in range(6):
        shrt+= random.choice(chr(random.randint(65,90))
                                +chr(random.randint(97,122))
                                +chr(random.randint(48,57))
                                )
    return shrt


def create_shortcode():
    shrt = code_gen()
    qs = bitly.objects.filter(shortcode__iexact=shrt)
    if qs.exists():
        return create_shortcode()
    else:
        return shrt
def goto(request,shortcode=None):
    qs=bitly.objects.get_object



