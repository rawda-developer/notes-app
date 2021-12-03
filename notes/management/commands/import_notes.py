from collections import Counter
import csv
from django.core.files.images import ImageFile
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from notes import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class Command(BaseCommand):
    help = 'Import Data in Notes app'

    def add_arguments(self, parser):
        parser.add_argument("csvfile", type=open)

    def handle(self, *args, **options):
        self.stdout.write("Importing notes")
        c = Counter()
        reader = csv.DictReader(options.pop("csvfile"))
        for row in reader:
            note, note_created = models.Notes.objects.get_or_create(
                title=row["title"], text=row["text"]
            )

            user = get_object_or_404(User, id=row['user_id'])
            
            note.user = user
            note.save()
            c["notes"] += 1
            if note_created:
                c["notes_created"] += 1

        self.stdout.write("Notes processed=%d (created=%d)" %
                          (c["notes"], c["notes_created"]))
