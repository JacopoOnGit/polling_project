import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'polling_api.settings')

import django
django.setup()

from django.core.management import call_command
call_command('migrate')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

