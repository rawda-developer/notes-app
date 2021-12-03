from collections import Counter
import csv
from django.core.files.images import ImageFile
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from notes import models
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Import Data in Notes app'

    def add_arguments(self, parser):
        parser.add_argument("csvfile", type=open)

    def handle(self, *args, **options):
        self.stdout.write("Importing users")
        c = Counter()
        reader = csv.DictReader(options.pop("csvfile"))
        for row in reader:
            user, user_created = User.objects.get_or_create(
                username=row["username"], password=row["password"]
            )
            # notes = models.Notes.objects.get_or_404(user=user)
            # user.notes = notes
            
            if user_created:
                c['users_created'] += 1
            c["users"] += 1

        self.stdout.write("Users processed=%d (created=%d)" %
                          (c["users"], c["users_created"]))
