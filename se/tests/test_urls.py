from django.test import SimpleTestCase
from django.urls import reverse, resolve

from se.views import SeListView, SeDetailView, SeCreateView, SeUpdateView, SeDeleteView

class TestUrls(SimpleTestCase):
    
    # Se
    def test_index_url_resolves(self):
        url = reverse('se:index')
        self.assertEqual(resolve(url).func.view_class, SeListView)

    def test_create_url_resolves(self):
        url = reverse('se:create')
        self.assertEqual(resolve(url).func.view_class, SeCreateView)

    def test_detail_url_resolves(self):
        url = reverse('se:detail', kwargs={'pk': 'some-pk'})
        self.assertEqual(resolve(url).func.view_class, SeDetailView)

    def test_update_url_resolves(self):
        url = reverse('se:update', kwargs={'pk': 'some-pk'})
        self.assertEqual(resolve(url).func.view_class, SeUpdateView)

    def test_delete_url_resolves(self):
        url = reverse('se:delete', args=['some-pk'])
        self.assertEqual(resolve(url).func.view_class, SeDeleteView)