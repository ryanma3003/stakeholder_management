from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from se.views import SeListView, SeDetailView, SeCreateView, SeUpdateView, SeDeleteView
from se.models import *
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
            field="Manufaktur",
            address="test",
            info="test",
            phone="01812812",
            email="asd@adsa.com",
            landing_page="",
            kode_pos="12312"
        )

        self.se1 = Se.objects.create(
            year=2022,
            indeks_nilai=36.0,
            indeks_ket="Tinggi",
            sistem="test",
            keterangan="test",
            month=self.month1,
            stakeholder=self.stakeholder1,
        )

        self.se_list_url = reverse('se:index')
        self.se_detail_url = reverse('se:detail', kwargs={'pk':self.se1.id})
        self.se_create_url = reverse('se:create')
        self.se_update_url = reverse('se:update', kwargs={'pk':self.se1.id})
        self.se_delete_url = reverse('se:delete', kwargs={'pk':self.se1.id})

        user = User.objects.create_superuser(username='d441')
        user.set_password('csirtd441')
        user.save()

        self.client.login(username='d441', password='csirtd441')

    def test_se_list_GET(self):
        response = self.client.get(self.se_list_url)
        self.assertEquals(response.status_code, 200)

    def test_se_detail_GET(self):
        response = self.client.get(self.se_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.se1.stakeholder.name, 'stakeholder1')

    def test_se_create_GET(self):
        response = self.client.get(self.se_create_url)
        self.assertEquals(response.status_code, 200)

    def test_se_update_GET(self):
        response = self.client.get(self.se_update_url)
        self.assertEquals(response.status_code, 200)

    def test_se_delete_DELETE_deletes_stakeholder(self):
        response = self.client.delete(self.se_delete_url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Se.objects.count(), 0)