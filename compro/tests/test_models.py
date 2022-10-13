from django.utils import timezone
from django.test import TestCase, Client
from compro.models import *
from workshop.models import Workshop
from django.contrib.auth.models import User

# Create your tests here.
class TestModels(TestCase):
    def setUp(self):
        self.client = Client()

        user = User.objects.create_superuser(
            username='d441', email='d441@bssn.go.id', password='my_secret')
            
        self.client.login(username='d441', password='csirtd441')

        self.stakeholder1 = Stakeholder.objects.create(
            name="stakeholder 1",
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

    def test_stakeholder_is_assigned_slug_on_creation(self):
        self.assertEquals(self.stakeholder1.slug, 'stakeholder-1')

    def test_sdm_model(self):
        Sdm.objects.create(
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

        self.assertEqual(Sdm.objects.count(), 1)

    def test_se_model(self):
        Sistemelektronik.objects.create(
            stakeholder= self.stakeholder1,
            nama= 'hp',
            spesifikasi= 'core i9',
            unit= '1',
            unit_pengelola= 'IT'
        )

        self.assertEqual(Sistemelektronik.objects.count(), 1)

    def test_pr_model(self):
        Prosedur.objects.create(
            stakeholder= self.stakeholder1,
            nama= 'test',
            nomer= '123123',
            status= 'RL',
            tahun= '2022'
        )

        self.assertEqual(Prosedur.objects.count(), 1)

    def test_lw_model(self):
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

        workshop1 = Workshop.objects.create(
            nama='workshop1',
            tanggal=timezone.now(),
            lokasi='Jakarta'
        )

        lw = ListWorkshop.objects.create(
            stakeholder= self.stakeholder1,
            workshop= workshop1,
            status= 'PS',
            level= 'int'
        )

        lw.sdm.set(get_sdm)
        lw.save()

        self.assertEqual(ListWorkshop.objects.count(), 1)