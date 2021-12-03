from django.test import TestCase
from django.urls import reverse


class TestPages(TestCase):
    def test_welcome_page_works(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/welcome.html')
        self.assertContains(response, 'Welcome to SmartNotes!')

    