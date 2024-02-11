from django.test import TestCase
from django.urls import reverse_lazy


class ContactFormTestCase(TestCase):

    def test_form_is_valid(self):
        data = {
            'name': 'Felicity Jones',
            'email': 'felicity@jones.com',
            'subject': 'Assunto Aqui',
            'message': 'Corpo do e-mail aqui'
        }
        response = self.client.post(reverse_lazy('index'), data)
        self.assertEqual(response.status_code, 302)

    def test_form_is_not_valid(self):
        data = {
            'name': 'Felicity Jones',
            'email': 'felicity',
            'subject': 'Assunto Aqui'
        }
        response = self.client.post(reverse_lazy('index'), data)
        self.assertEqual(response.status_code, 200)
