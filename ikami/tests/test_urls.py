from django.test import SimpleTestCase
from django.urls import reverse, resolve

from ikami.views import *

class TestUrls(SimpleTestCase):
    
    # Se
    def test_index_url_resolves(self):
        url = reverse('ikami:index')
        self.assertEqual(resolve(url).func.view_class, IkamiListView)

    def test_create_url_resolves(self):
        url = reverse('ikami:create')
        self.assertEqual(resolve(url).func.view_class, IkamiCreateView)

    def test_detail_url_resolves(self):
        url = reverse('ikami:detail', kwargs={'pk': 'some-pk'})
        self.assertEqual(resolve(url).func.view_class, IkamiDetailView)

    def test_update_url_resolves(self):
        url = reverse('ikami:update', kwargs={'pk': 'some-pk'})
        self.assertEqual(resolve(url).func.view_class, IkamiUpdateView)

    def test_delete_url_resolves(self):
        url = reverse('ikami:delete', args=['some-pk'])
        self.assertEqual(resolve(url).func.view_class, IkamiDeleteView)