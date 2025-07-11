"""
WSGI config for polling_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# ESEGUE MIGRAZIONI AUTOMATICHE IN PRODUZIONE
import django
django.setup()
from django.core.management import call_command
call_command('migrate')


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'polling_api.settings')

application = get_wsgi_application()
