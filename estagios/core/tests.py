from django.test import TestCase
from django.shortcuts import reverse

class Index_Test(TestCase):
    def test_index_status_code(self):
        response = self.client.get(reverse('core:index'))
        self.assertEqual(response.status_code, 200)

class RootTest(TestCase):
    def test_root_status_code(self):
        response2 = self.client.get(reverse('core:root'), follow=True)
        self.assertEqual(response2.status_code, 200)
    
    def test_root_redirect(self):
        response = self.client.get(reverse('core:root'))
        self.assertEqual(response.status_code, 302)