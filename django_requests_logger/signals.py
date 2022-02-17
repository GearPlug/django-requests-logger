from django.dispatch import Signal
from django.utils import version

if version.get_version() < '4.0.0':
    response_is_ok = Signal(providing_args=['instance'])
    response_is_not_ok = Signal(providing_args=['instance'])
else:
    response_is_ok = Signal()
    response_is_not_ok = Signal()
