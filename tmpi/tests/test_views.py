from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from tmpi.models import *
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

        self.tmpi = Tmpi.objects.create(
            year=2022,
            month=self.month1,
            stakeholder=self.stakeholder1,

            file_tmpi= "ttis_evaluasi/tmpi.xlsx",
            penilaian_kritikalitas= 3,
            analisis_ancaman= 3,
            orang_proses_teknologi= 3,
            lingkungan_kontrol= 3,
            penilaian_kematangan= 3,
            total_fase_1= 3,
            identifikasi_respon= 3,
            penyelidikan= 3,
            aksi= 3,
            pemulihan= 3,
            total_fase_2= 3,
            identifikasi_tindak_lanjut= 3,
            pelaporan_review= 3,
            pembelajaran= 3,
            pembaruan_informasi= 3,
            analisis_tren= 3,
            total_fase_3= 3,
            nilai_akhir= 3,
        )

        self.tmpi_list_url = reverse('tmpi:index')
        self.tmpi_detail_url = reverse('tmpi:detail', kwargs={'pk':self.tmpi.id})
        self.tmpi_create_url = reverse('tmpi:create')
        self.tmpi_update_url = reverse('tmpi:update', kwargs={'pk':self.tmpi.id})
        self.tmpi_delete_url = reverse('tmpi:delete', kwargs={'pk':self.tmpi.id})

        user = User.objects.create_superuser(username='d441')
        user.set_password('csirtd441')
        user.save()

        self.client.login(username='d441', password='csirtd441')

    def test_tmpi_list_GET(self):
        response = self.client.get(self.tmpi_list_url)
        self.assertEquals(response.status_code, 200)

    def test_tmpi_detail_GET(self):
        response = self.client.get(self.tmpi_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.tmpi.stakeholder.name, 'stakeholder1')

    def test_tmpi_create_GET(self):
        response = self.client.get(self.tmpi_create_url)
        self.assertEquals(response.status_code, 200)

    def test_tmpi_update_GET(self):
        response = self.client.get(self.tmpi_update_url)
        self.assertEquals(response.status_code, 200)

    def test_tmpi_delete_DELETE_deletes_stakeholder(self):
        response = self.client.delete(self.tmpi_delete_url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Tmpi.objects.count(), 0)