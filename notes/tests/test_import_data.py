from io import StringIO
from django.conf import settings
from django.core.management import call_command
from django.test import TestCase, override_settings
from notes import models
from django.contrib.auth.models import User

class TestImport(TestCase):
    def test_import_data(self):
        out = StringIO()
        args = ['notes/management/commands/users.csv']
        call_command('import_users', *args, stdout=out)
        expected_out = ("Importing users\n"
                        "Users processed=4 (created=4)\n")
        self.assertEqual(out.getvalue(), expected_out)
        self.assertEqual(User.objects.count(), 4)
        out = StringIO()
        args = ['notes/management/commands/notes.csv']
        call_command('import_notes', *args, stdout=out)
        expected_out = ("Importing notes\n"
                       "Notes processed=6 (created=6)\n")
        self.assertEqual(out.getvalue(), expected_out)
        self.assertEqual(models.Notes.objects.count(), 6)

