from __future__ import absolute_import, unicode_literals
from os import environ

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

WEBPACK_DEV_SERVER = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
