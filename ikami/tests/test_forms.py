from django.test import TestCase
from ikami.forms import IkamiForm
from month.models import Month
from compro.models import Stakeholder

# Create your tests here.
class TestForms(TestCase):
    def setUp(self):
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

    def test_se_form_valid_data(self):
        form = IkamiForm(data={
            "year":2022,
            "tata_kelola":50,
            "pengelolaan_risiko":50,
            "kerangka_kerja":50,
            "pengelolaan_aset":50,
            "teknologi_keamanan":50,
            "keterlibatan_pihak_ketiga":None,
            "layanan_infrastruktur_awan":None,
            "data_pribadi":None,
            "month":self.month1.id,
            "stakeholder":self.stakeholder1.id,
        })

        self.assertTrue(form.is_valid())

    def test_se_form_no_data(self):
        form = IkamiForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 8)