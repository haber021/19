from django.core.management.base import BaseCommand
from django.utils import timezone
from authentication.models import EmailLink

class Command(BaseCommand):
    help = 'Mark expired email links'

    def handle(self, *args, **kwargs):
        expired_links = EmailLink.objects.filter(created_at__lt=timezone.now() - timezone.timedelta(minutes=30), is_active=True)
        expired_links.update(is_active=False)
        self.stdout.write(self.style.SUCCESS('Expired email links marked successfully.'))