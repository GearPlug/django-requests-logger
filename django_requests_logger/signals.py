from django.dispatch import Signal

response_is_ok = Signal(providing_args=['instance'])
response_is_not_ok = Signal(providing_args=['instance'])
