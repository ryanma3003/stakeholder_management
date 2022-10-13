from django.utils import timezone
from django.test import RequestFactory, TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User

from compro.forms import *
from compro.models import *
from workshop.models import Workshop

from compro.views import *

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

        user = User.objects.create_superuser(username='d441')
        user.set_password('csirtd441')
        user.save()

        self.client.login(username='d441', password='csirtd441')

        self.stakeholder1 = Stakeholder.objects.create(
            name="stakeholder1",
            type="BUMN",
            field="IN",
            address="test",
            info="test",
            phone="01812812",
            email="asd@adsa.com",
            landing_page="",
            kode_pos="12312",
            image="stakeholder_logo/test.png",
            pic=user
        )

        self.compro_list_url = reverse('stakeholder:index')
        self.compro_detail_url = reverse('stakeholder:detail', kwargs={'pk':self.stakeholder1.id})
        self.compro_create_url = reverse('stakeholder:create')
        self.compro_update_url = reverse('stakeholder:update', kwargs={'pk':self.stakeholder1.id})
        self.compro_delete_url = reverse('stakeholder:delete', kwargs={'pk':self.stakeholder1.id})

        self.compro_sdm_create_url = '%s?s_id=%s' % (reverse('stakeholder:sdm_create'), self.stakeholder1.id)
        self.compro_se_create_url = '%s?s_id=%s' % (reverse('stakeholder:se_create'), self.stakeholder1.id)
        self.compro_pr_create_url = '%s?s_id=%s' % (reverse('stakeholder:pr_create'), self.stakeholder1.id)
        self.compro_lw_create_url = '%s?s_id=%s' % (reverse('stakeholder:lw_create'), self.stakeholder1.id)

    def test_compro_list_GET(self):
        response = self.client.get(self.compro_list_url)
        self.assertEquals(response.status_code, 200)

    def test_compro_detail_GET(self):
        response = self.client.get(self.compro_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.stakeholder1.name, 'stakeholder1')

    def test_compro_create_GET(self):
        response = self.client.get(self.compro_create_url)
        self.assertEquals(response.status_code, 200)

    def test_compro_update_GET(self):
        response = self.client.get(self.compro_update_url)
        self.assertEquals(response.status_code, 200)

    def test_compro_delete_DELETE_deletes_stakeholder(self):
        response = self.client.delete(self.compro_delete_url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Stakeholder.objects.count(), 0)

    def test_compro_sdm_create_POST_adds_new_sdm(self):
        response = self.client.post(self.compro_sdm_create_url, {
            'stakeholder': self.stakeholder1.id,
            'nama': 'Tony',
            'jabatan': 'manager',
            'unit_kerja': 'IT',
            'kompetensi': 'network',
            'sertifikat': 'CCNA',
            'telepon': '0912830182',
            'email': 'asd@gmail.com',
            'csirt': 'yes',
            'narahubung': 'no',
            'gender': 'm'
        })
        
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Sdm.objects.filter(nama='Tony').count(), 1)

    def test_compro_sdm_delete_DELETE_deletes_sdm(self):
        sdm_delete = Sdm.objects.create(
            stakeholder= self.stakeholder1,
            nama= 'Alex',
            jabatan= 'manager',
            unit_kerja= 'IT',
            kompetensi= 'network',
            sertifikat= 'CCNA',
            telepon= '0912830182',
            email= 'asd@gmail.com',
            csirt= 'yes',
            narahubung= 'no',
            gender= 'm'
        )

        url = '%s?s_id=%s' % (reverse('stakeholder:sdm_delete', kwargs={'pk':sdm_delete.id}), self.stakeholder1.id)

        response = self.client.delete(url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Sdm.objects.count(), 0)

    def test_compro_se_create_POST_adds_new_se(self):
        response = self.client.post(self.compro_se_create_url, {
            'stakeholder': self.stakeholder1.id,
            'nama': 'lenovo server',
            'spesifikasi': 'core i9',
            'unit': '1',
            'unit_pengelola': 'IT'
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Sistemelektronik.objects.filter(nama='lenovo server').count(), 1)

    def test_compro_se_delete_DELETE_deletes_se(self):
        se_delete = Sistemelektronik.objects.create(
            stakeholder= self.stakeholder1,
            nama= 'hp',
            spesifikasi= 'core i9',
            unit= '1',
            unit_pengelola= 'IT'
        )

        url = '%s?s_id=%s' % (reverse('stakeholder:se_delete', kwargs={'pk':se_delete.id}), self.stakeholder1.id)

        response = self.client.delete(url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Sistemelektronik.objects.count(), 0)

    def test_compro_pr_create_POST_adds_new_pr(self):
        response = self.client.post(self.compro_pr_create_url, {
            'stakeholder': self.stakeholder1.id,
            'nama': 'test',
            'nomer': '123123',
            'status': 'PB',
            'tahun': '2022',
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Prosedur.objects.filter(nama='test').count(), 1)

    def test_compro_pr_delete_DELETE_deletes_pr(self):
        pr_delete = Prosedur.objects.create(
            stakeholder= self.stakeholder1,
            nama= 'test',
            nomer= '123123',
            status= 'RL',
            tahun= '2022'
        )

        url = '%s?s_id=%s' % (reverse('stakeholder:pr_delete', kwargs={'pk':pr_delete.id}), self.stakeholder1.id)

        response = self.client.delete(url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Prosedur.objects.count(), 0)

    def test_compro_lw_create_POST_adds_new_lw(self):
        sdm1 = Sdm.objects.create(
            stakeholder= self.stakeholder1,
            nama= 'Alex',
            jabatan= 'manager',
            unit_kerja= 'IT',
            kompetensi= 'network',
            sertifikat= 'CCNA',
            telepon= '0912830182',
            email= 'asd@gmail.com',
            csirt= 'yes',
            narahubung= 'no',
            gender= 'm'
        )

        workshop1 = Workshop.objects.create(
            nama='workshop1',
            tanggal=timezone.now(),
            lokasi='Jakarta'
        )

        response = self.client.post(self.compro_lw_create_url, {
            'stakeholder': self.stakeholder1.id,
            'sdm': sdm1.id,
            'workshop': workshop1.id,
            'status': 'PS',
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(ListWorkshop.objects.filter(stakeholder=self.stakeholder1.id).count(), 1)

    def test_compro_lw_delete_DELETE_deletes_lw(self):
        sdm1 = Sdm.objects.create(
            stakeholder= self.stakeholder1,
            nama= 'Alex',
            jabatan= 'manager',
            unit_kerja= 'IT',
            kompetensi= 'network',
            sertifikat= 'CCNA',
            telepon= '0912830182',
            email= 'asd@gmail.com',
            csirt= 'yes',
            narahubung= 'no',
            gender= 'm'
        )
        sdm2 = Sdm.objects.create(
            stakeholder= self.stakeholder1,
            nama= 'John',
            jabatan= 'staff',
            unit_kerja= 'IT',
            kompetensi= 'network',
            sertifikat= 'CCNA',
            telepon= '123123123',
            email= 'hawa@gmail.com',
            csirt= 'yes',
            narahubung= 'no',
            gender= 'm'
        )

        get_sdm = Sdm.objects.filter(stakeholder_id = self.stakeholder1)


        workshop_lw_delete = Workshop.objects.create(
            nama='workshop1',
            tanggal=timezone.now(),
            lokasi='Jakarta'
        )

        lw_delete = ListWorkshop.objects.create(
            stakeholder= self.stakeholder1,
            workshop= workshop_lw_delete,
            status= 'PS',
            level= 'int'
        )

        lw_delete.sdm.set(get_sdm)
        lw_delete.save()

        url = '%s?s_id=%s' % (reverse('stakeholder:lw_delete', kwargs={'pk':lw_delete.id}), self.stakeholder1.id)

        response = self.client.delete(url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(ListWorkshop.objects.count(), 0)