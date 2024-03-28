# In your Celery configuration file (e.g., celery.py or tasks.py)

from celery import Celery
from celery.schedules import crontab

app = Celery('mysite')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Schedule the mark_expired_links command to run every 5 minutes
app.conf.beat_schedule = {
    'mark-expired-links': {
        'task': 'authentication.tasks.mark_expired_links',
        'schedule': crontab(minute='*/5'),
    },
}
