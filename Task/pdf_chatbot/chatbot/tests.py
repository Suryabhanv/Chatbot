from django.test import TestCase

# Create your tests here.

from django.test import TestCase, Client
from django.urls import reverse
from .models import PDFFile

class PDFUploadTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_upload_pdf(self):
        with open('test.pdf', 'rb') as pdf:
            response = self.client.post(reverse('upload'), {'file': pdf})
            self.assertEqual(response.status_code, 302)  # Redirect after successful upload

    def test_chat_with_pdf(self):
        # Assume a PDF has been uploaded and content indexed
        response = self.client.post(reverse('chat'), {'query': 'What is the main topic?'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('answer', response.json())
