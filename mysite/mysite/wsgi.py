"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append('/home/bitnami/venvs/blog/mysite')
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings.dev")
os.environ.setdefault("PYTHON_EGG_CACHE", "/home/bitnami/venvs/blog/mysite/egg_cache")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
