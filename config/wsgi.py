"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Run database migrations automatically when starting up on Vercel
if "VERCEL" in os.environ:
    from django.core.management import call_command
    import django
    django.setup()
    try:
        call_command('migrate', interactive=False)
    except Exception as e:
        print("Error running migrations on startup:", e)

application = get_wsgi_application()
app = application
