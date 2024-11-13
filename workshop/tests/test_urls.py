from django.test import SimpleTestCase
from django.urls import reverse, resolve

from workshop.views import *

class TestUrls(SimpleTestCase):
    
    # Se
    def test_index_url_resolves(self):
        url = reverse('workshop:index')
        self.assertEqual(resolve(url).func.view_class, WorkshopListView)

    def test_create_url_resolves(self):
        url = reverse('workshop:create')
        self.assertEqual(resolve(url).func.view_class, WorkshopCreateView)

    def test_detail_url_resolves(self):
        url = reverse('workshop:detail', kwargs={'pk': 'some-pk'})
        self.assertEqual(resolve(url).func.view_class, WorkshopDetailView)

    def test_update_url_resolves(self):
        url = reverse('workshop:update', kwargs={'pk': 'some-pk'})
        self.assertEqual(resolve(url).func.view_class, WorkshopUpdateView)

    def test_delete_url_resolves(self):
        url = reverse('workshop:delete', args=['some-pk'])
        self.assertEqual(resolve(url).func.view_class, WorkshopDeleteView)