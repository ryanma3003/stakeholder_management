from django.test import SimpleTestCase
from django.urls import reverse, resolve

from tmpi.views import *

class TestUrls(SimpleTestCase):
    
    # Se
    def test_index_url_resolves(self):
        url = reverse('tmpi:index')
        self.assertEqual(resolve(url).func.view_class, TmpiListView)

    def test_create_url_resolves(self):
        url = reverse('tmpi:create')
        self.assertEqual(resolve(url).func.view_class, TmpiCreateView)

    def test_detail_url_resolves(self):
        url = reverse('tmpi:detail', kwargs={'pk': 'some-pk'})
        self.assertEqual(resolve(url).func.view_class, TmpiDetailView)

    def test_update_url_resolves(self):
        url = reverse('tmpi:update', kwargs={'pk': 'some-pk'})
        self.assertEqual(resolve(url).func.view_class, TmpiUpdateView)

    def test_delete_url_resolves(self):
        url = reverse('tmpi:delete', args=['some-pk'])
        self.assertEqual(resolve(url).func.view_class, TmpiDeleteView)