"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import os
import sys

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

path = os.path.expanduser('~/My-Virtual-Blog')
if path not in sys.path:
    sys.path.append(path)

os.environ("DJANGO_SETTINGS_MODULE", "My-Virtual-Blog.settings")


application = StaticFilesHandler(get_wsgi_application())

application = DjangoWhiteNoise(application)
