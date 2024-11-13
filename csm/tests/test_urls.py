from django.test import SimpleTestCase
from django.urls import reverse, resolve

from csm.views import *

class TestUrls(SimpleTestCase):
    
    # Se
    def test_index_url_resolves(self):
        url = reverse('csm:index')
        self.assertEqual(resolve(url).func.view_class, CsmListView)

    def test_create_url_resolves(self):
        url = reverse('csm:create')
        self.assertEqual(resolve(url).func.view_class, CsmCreateView)

    def test_detail_url_resolves(self):
        url = reverse('csm:detail', kwargs={'pk': 'some-pk'})
        self.assertEqual(resolve(url).func.view_class, CsmDetailView)

    def test_update_url_resolves(self):
        url = reverse('csm:update', kwargs={'pk': 'some-pk'})
        self.assertEqual(resolve(url).func.view_class, CsmUpdateView)

    def test_delete_url_resolves(self):
        url = reverse('csm:delete', args=['some-pk'])
        self.assertEqual(resolve(url).func.view_class, CsmDeleteView)