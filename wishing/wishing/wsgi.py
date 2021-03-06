"""
WSGI config for wishing project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# 这里设置 'DJANGO_SETTINGS_MODULE'，至关重要，影响django加载settings的位置
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wishing.settings")
os.environ.setdefault("LANG", "en_us.UTF-8")

application = get_wsgi_application()
