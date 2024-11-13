from django.test import TestCase
from se.forms import SeForm
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
        form = SeForm(data={
            "year": 2022,
            "month": self.month1.id,
            "stakeholder": self.stakeholder1.id,
            "indeks_nilai": 36.0,
            "indeks_ket": "Tinggi",
            "sistem": "test",
            "jenis_usaha": "Test",
            "keterangan": "test",
            "nilai_investasi": "a",
            "total_anggaran": "a",
            "kewajiban": "a",
            "kriptografi": "a",
            "pengguna": "a",
            "data_pribadi": "a",
            "kritis_data": "a",
            "kritis_proses" : "a",
            "dampak_kegagalan" : "a",
            "potensi_kerugian" : "a",
            
            "bobot_nilai_investasi": "2",
            "bobot_total_anggaran": "2",
            "bobot_kewajiban": "2",
            "bobot_kriptografi": "2",
            "bobot_pengguna": "2",
            "bobot_data_pribadi": "2",
            "bobot_kritis_data": "2",
            "bobot_kritis_proses": "2",
            "bobot_dampak_kegagalan": "2",
            "bobot_potensi_kerugian": "2"
        })

        self.assertTrue(form.is_valid())

    def test_se_form_no_data(self):
        form = SeForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 14)