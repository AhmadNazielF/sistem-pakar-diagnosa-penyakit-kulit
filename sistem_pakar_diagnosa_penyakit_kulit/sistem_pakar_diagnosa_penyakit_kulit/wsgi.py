"""
WSGI config for sistem_pakar_diagnosa_penyakit_kulit project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistem_pakar_diagnosa_penyakit_kulit.settings')

application = get_wsgi_application()
