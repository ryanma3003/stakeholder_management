from django.test import TestCase
from compro.forms import *
from compro.models import *
from workshop.models import Workshop

from django.utils import timezone


# Create your tests here.
class TestForms(TestCase):
    def setUp(self):
        self.stakeholder1 = Stakeholder.objects.create(
            name="stakeholder test",
            type="BUMN",
            field="Manufaktur",
            address="test",
            info="test",
            phone="01812812",
            email="asd@adsa.com",
            landing_page="",
            kode_pos="12312"
        )

    def get_form_kwargs(self):
        kwargs = {'s_id': self.stakeholder1.id}
        return kwargs

    def test_stakeholder_form_valid_data(self):
        form = ComproForm(data={
            "name":"stakeholder1",
            "type":"BUMN",
            "field":"Manufaktur",
            "address":"test",
            "info":"test",
            "phone":"01812812",
            "email":"asd@adsa.com",
            "landing_page":"",
            "kode_pos":"12312"
        })

        self.assertTrue(form.is_valid())

    def test_stakeholder_form_no_data(self):
        form = ComproForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 6)

    def test_sdm_form_valid_data(self):
        form = SdmForm(data={
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

        self.assertTrue(form.is_valid())

    def test_sdm_form_no_data(self):
        form = SdmForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)

    def test_se_form_valid_data(self):
        form = SistemelektronikForm(data={
            'stakeholder': self.stakeholder1.id,
            'nama': 'lenovo server',
            'spesifikasi': 'core i9',
            'unit': '1',
            'unit_pengelola': 'IT'
        })

        self.assertTrue(form.is_valid())

    def test_se_form_no_data(self):
        form = SistemelektronikForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_pr_form_valid_data(self):
        form = ProsedurForm(data={
            'stakeholder': self.stakeholder1.id,
            'nama': 'test',
            'nomer': '123123',
            'status': 'PB',
            'tahun': '2022',
        })

        self.assertTrue(form.is_valid())

    def test_pr_form_no_data(self):
        form = ProsedurForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    def test_lw_form_valid_data(self):
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

        form = ListWorkshopForm(data={
            'stakeholder': self.stakeholder1.id,
            'sdm': sdm1.id,
            'workshop': workshop1.id,
            'status': 'PS',
        }, **self.get_form_kwargs())

        self.assertTrue(form.is_valid())

    def test_lw_form_no_data(self):
        form = ListWorkshopForm(data={}, **self.get_form_kwargs())

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)