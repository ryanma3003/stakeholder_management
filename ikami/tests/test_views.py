from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from ikami.views import *
from ikami.models import *
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

        self.ikami1 = Ikami.objects.create(
            year=2022,
            tata_kelola=100,
            pengelolaan_risiko=200,
            kerangka_kerja=300,
            pengelolaan_aset=150,
            teknologi_keamanan=100,
            keterlibatan_pihak_ketiga=None,
            layanan_infrastruktur_awan=None,
            data_pribadi=None,
            month=self.month1,
            stakeholder=self.stakeholder1,
        )

        self.ikami_list_url = reverse('ikami:index')
        self.ikami_detail_url = reverse('ikami:detail', kwargs={'pk':self.ikami1.id})
        self.ikami_create_url = reverse('ikami:create')
        self.ikami_update_url = reverse('ikami:update', kwargs={'pk':self.ikami1.id})
        self.ikami_delete_url = reverse('ikami:delete', kwargs={'pk':self.ikami1.id})

        user = User.objects.create_superuser(username='d441')
        user.set_password('csirtd441')
        user.save()

        self.client.login(username='d441', password='csirtd441')

    def test_ikami_list_GET(self):
        response = self.client.get(self.ikami_list_url)
        self.assertEquals(response.status_code, 200)

    def test_ikami_detail_GET(self):
        response = self.client.get(self.ikami_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.ikami1.stakeholder.name, 'stakeholder1')

    def test_ikami_create_GET(self):
        response = self.client.get(self.ikami_create_url)
        self.assertEquals(response.status_code, 200)

    def test_ikami_update_GET(self):
        response = self.client.get(self.ikami_update_url)
        self.assertEquals(response.status_code, 200)

    def test_ikami_delete_DELETE_deletes_stakeholder(self):
        response = self.client.delete(self.ikami_delete_url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Ikami.objects.count(), 0)