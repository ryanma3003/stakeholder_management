from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from csm.views import *
from csm.models import *
from compro.models import Stakeholder
from month.models import Month


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.month1 = Month.objects.create(
            month_id="Januari",
            month_en="January",
            month_abb="Jan",
        )

        self.stakeholder1 = Stakeholder.objects.create(
            name="stakeholder1",
            type="BUMN",
            field="IN",
            address="test",
            info="test",
            phone="01812812",
            email="asd@adsa.com",
            landing_page="",
            kode_pos="12312"
        )

        self.csm1 = Csm.objects.create(
            year=2022,
            kesadaran=4,
            audit=4,
            kontrol=3,
            pemenuhan=3,
            kebijakan=2,
            proses=2,
            manajemen_aset=3,
            inventaris=4,
            manajemen_risiko=3,
            prioritas=3,
            pelaporan_identifikasi=3,
            klasifikasi=4,
            jaringan=4,
            aplikasi=4,
            pengguna=2,
            manajemen_identitas=4,
            cloud=3,
            data=4,
            perubahan=3,
            monitor=5,
            peringatan=4,
            pemberitahuan=3,
            intelijen=3,
            pelaporan_deteksi=4,
            penahanan=4,
            penanggulanan=3,
            pemulihan=4,
            kegiatan_pasca=3,
            pelaporan_respon=3,
            month=self.month1,
            stakeholder=self.stakeholder1,
        )

        self.csm_list_url = reverse('csm:index')
        self.csm_detail_url = reverse('csm:detail', kwargs={'pk':self.csm1.id})
        self.csm_create_url = reverse('csm:create')
        self.csm_update_url = reverse('csm:update', kwargs={'pk':self.csm1.id})
        self.csm_delete_url = reverse('csm:delete', kwargs={'pk':self.csm1.id})

        user = User.objects.create_superuser(username='d441')
        user.set_password('csirtd441')
        user.save()

        self.client.login(username='d441', password='csirtd441')

    def test_csm_list_GET(self):
        response = self.client.get(self.csm_list_url)
        self.assertEqual(response.status_code, 200)

    def test_csm_detail_GET(self):
        response = self.client.get(self.csm_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.csm1.stakeholder.name, 'stakeholder1')

    def test_csm_create_GET(self):
        response = self.client.get(self.csm_create_url)
        self.assertEqual(response.status_code, 200)

    def test_csm_update_GET(self):
        response = self.client.get(self.csm_update_url)
        self.assertEqual(response.status_code, 200)

    def test_csm_delete_DELETE_deletes_stakeholder(self):
        response = self.client.delete(self.csm_delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Csm.objects.count(), 0)