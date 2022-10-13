from django.test import SimpleTestCase
from django.urls import reverse, resolve

from phrasalword.views import *

class TestUrls(SimpleTestCase):
    
    # Phrasalword
    def test_index_url_resolves(self):
        url = reverse('profile:show_pass')
        self.assertEqual(url, '/profile/show_pass')

    def test_update_url_resolves(self):
        url = reverse('profile:update', kwargs={'pk': 'some-pk'})
        self.assertEqual(resolve(url).func.view_class, PhrasalwordUpdateView)