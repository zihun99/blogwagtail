import os
import sys
sys.path.append('/home/bitnami/venvs/blog/mysite/')
os.environ.setdefault("PYTHON_EGG_CACHE", "/home/bitnami/venvs/blog/mysite/egg_cache")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutorial.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

