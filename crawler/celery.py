import os
from xml.etree.ElementInclude import include 
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crawler.settings')

app = Celery('crawler', include=['crawler.tasks'])

# locate the config module of celery ,and namespace is used for prefix of each config attribute.
app.config_from_object('django.conf.settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()



