from django.core.management.base import BaseCommand
from sample_app.models import User  # Import your custom User model

class Command(BaseCommand):
    help = 'Delete all users from the database'

    def handle(self, *args, **kwargs):
        User.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all users'))
