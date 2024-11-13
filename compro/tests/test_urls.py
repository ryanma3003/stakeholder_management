from django.test import SimpleTestCase
from django.urls import reverse, resolve

# import views
from compro.views import (
    ComproListView, 
    ComproDetailView, 
    ComproCreateView, 
    ComproUpdateView,
    ComproDeleteView,
    SdmCreateView,
    SdmUpdateView,
    SdmDeleteView,
    SistemelektronikCreateView,
    SistemelektronikUpdateView,
    SistemelektronikDeleteView,
    ProsedurCreateView,
    ProsedurUpdateView,
    ProsedurDeleteView,
    ListWorkshopCreateView,
    ListWorkshopUpdateView,
    ListWorkshopDeleteView,
    )

class TestUrls(SimpleTestCase):

    # Stakeholder
    def test_index_url_resolves(self):
        url = reverse('stakeholder:index')
        self.assertEqual(resolve(url).func.view_class, ComproListView)

    def test_create_url_resolves(self):
        url = reverse('stakeholder:create')
        self.assertEqual(resolve(url).func.view_class, ComproCreateView)

    def test_detail_url_resolves(self):
        url = reverse('stakeholder:detail', kwargs={'pk': 'some-pk'})
        self.assertEqual(resolve(url).func.view_class, ComproDetailView)

    def test_update_url_resolves(self):
        url = reverse('stakeholder:update', kwargs={'pk': 'some-pk'})
        self.assertEqual(resolve(url).func.view_class, ComproUpdateView)

    def test_delete_url_resolves(self):
        url = reverse('stakeholder:delete', args=['some-pk'])
        self.assertEqual(resolve(url).func.view_class, ComproDeleteView)

    # SDM
    def test_sdm_create_url_resolves(self):
        url = reverse('stakeholder:sdm_create')
        self.assertEqual(resolve(url).func.view_class, SdmCreateView)

    def test_sdm_update_url_resolves(self):
        url = reverse('stakeholder:sdm_update', kwargs={'pk': 'some-pk'})
        self.assertEqual(resolve(url).func.view_class, SdmUpdateView)

    def test_sdm_delete_url_resolves(self):
        url = reverse('stakeholder:sdm_delete', args=['some-pk'])
        self.assertEqual(resolve(url).func.view_class, SdmDeleteView)

    # Sistem Elektronik
    def test_se_create_url_resolves(self):
        url = reverse('stakeholder:se_create')
        self.assertEqual(resolve(url).func.view_class, SistemelektronikCreateView)

    def test_se_update_url_resolves(self):
        url = reverse('stakeholder:se_update', kwargs={'pk': 'some-pk'})
        self.assertEqual(resolve(url).func.view_class, SistemelektronikUpdateView)

    def test_se_delete_url_resolves(self):
        url = reverse('stakeholder:se_delete', args=['some-pk'])
        self.assertEqual(resolve(url).func.view_class, SistemelektronikDeleteView)

    # Prosedur
    def test_pr_create_url_resolves(self):
        url = reverse('stakeholder:pr_create')
        self.assertEqual(resolve(url).func.view_class, ProsedurCreateView)

    def test_pr_update_url_resolves(self):
        url = reverse('stakeholder:pr_update', kwargs={'pk': 'some-pk'})
        self.assertEqual(resolve(url).func.view_class, ProsedurUpdateView)

    def test_pr_delete_url_resolves(self):
        url = reverse('stakeholder:pr_delete', args=['some-pk'])
        self.assertEqual(resolve(url).func.view_class, ProsedurDeleteView)

    # Workshop
    def test_lw_create_url_resolves(self):
        url = reverse('stakeholder:lw_create')
        self.assertEqual(resolve(url).func.view_class, ListWorkshopCreateView)

    def test_lw_update_url_resolves(self):
        url = reverse('stakeholder:lw_update', kwargs={'pk': 'some-pk'})
        self.assertEqual(resolve(url).func.view_class, ListWorkshopUpdateView)

    def test_lw_delete_url_resolves(self):
        url = reverse('stakeholder:lw_delete', args=['some-pk'])
        self.assertEqual(resolve(url).func.view_class, ListWorkshopDeleteView)
