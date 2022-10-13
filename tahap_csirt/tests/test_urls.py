from django.test import SimpleTestCase
from django.urls import reverse, resolve

# import views
from tahap_csirt.views import *

class TestUrls(SimpleTestCase):

    # Edukasi

    def test_edu_create_url_resolves(self):
        url = reverse('ttis:edu_create')
        self.assertEqual(resolve(url).func.view_class, EdukasiCreateView)

    def test_edu_update_url_resolves(self):
        url = reverse('ttis:edu_update', kwargs={'pk': 'some-pk'})
        self.assertEqual(resolve(url).func.view_class, EdukasiUpdateView)

    def test_edu_delete_url_resolves(self):
        url = reverse('ttis:edu_delete', args=['some-pk'])
        self.assertEqual(resolve(url).func.view_class, EdukasiDeleteView)

    # Perencanaan
    def test_prn_create_url_resolves(self):
        url = reverse('ttis:prn_create')
        self.assertEqual(resolve(url).func.view_class, PerencanaanCreateView)

    def test_prn_update_url_resolves(self):
        url = reverse('ttis:prn_update', kwargs={'pk': 'some-pk'})
        self.assertEqual(resolve(url).func.view_class, PerencanaanUpdateView)

    def test_prn_delete_url_resolves(self):
        url = reverse('ttis:prn_delete', args=['some-pk'])
        self.assertEqual(resolve(url).func.view_class, PerencanaanDeleteView)

    # Penerapan
    def test_pnr_create_url_resolves(self):
        url = reverse('ttis:pnr_create')
        self.assertEqual(resolve(url).func.view_class, PenerapanCreateView)

    def test_pnr_update_url_resolves(self):
        url = reverse('ttis:pnr_update', kwargs={'pk': 'some-pk'})
        self.assertEqual(resolve(url).func.view_class, PenerapanUpdateView)

    def test_pnr_show_url_resolves(self):
        url = reverse('ttis:pnr_show', args=[1])
        self.assertEqual(url, '/ttis/penerapan/show/1')

    def test_pnr_delete_url_resolves(self):
        url = reverse('ttis:pnr_delete', args=['some-pk'])
        self.assertEqual(resolve(url).func.view_class, PenerapanDeleteView)

    # Penguatan
    def test_png_create_url_resolves(self):
        url = reverse('ttis:png_create')
        self.assertEqual(resolve(url).func.view_class, PenguatanCreateView)

    def test_png_update_url_resolves(self):
        url = reverse('ttis:png_update', kwargs={'pk': 'some-pk'})
        self.assertEqual(resolve(url).func.view_class, PenguatanUpdateView)

    def test_png_delete_url_resolves(self):
        url = reverse('ttis:png_delete', args=['some-pk'])
        self.assertEqual(resolve(url).func.view_class, PenguatanDeleteView)

    # Evaluasi
    def test_eva_create_url_resolves(self):
        url = reverse('ttis:eva_create')
        self.assertEqual(resolve(url).func.view_class, EvaluasiCreateView)

    def test_eva_update_url_resolves(self):
        url = reverse('ttis:eva_update', kwargs={'pk': 'some-pk'})
        self.assertEqual(resolve(url).func.view_class, EvaluasiUpdateView)

    def test_eva_delete_url_resolves(self):
        url = reverse('ttis:eva_delete', args=['some-pk'])
        self.assertEqual(resolve(url).func.view_class, EvaluasiDeleteView)
