from __future__ import absolute_import, unicode_literals

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_postgres_docker_celery_rabbitmq.settings')

app = Celery('django_postgres_docker_celery_rabbitmq',
             broker='amqp://rabbitmq',
             backend='amqp://rabbitmq',
             )

app.config_from_object('django.conf:settings', namespace='CELERY')
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()