"""
WSGI config for supermarket project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Supermarketi.settings')

application = Cling(get_wsgi_application())
application = WhiteNoise(application, root='Supermarketi/static')
application.add_files('Supermarketi/static', prefix='files/')