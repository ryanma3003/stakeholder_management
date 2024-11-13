from django.test import TestCase
from tmpi.forms import TmpiForm
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

    def test_tmpi_form_valid_data(self):
        form = TmpiForm(data={
            "year": 2022,
            "month": self.month1.id,
            "stakeholder": self.stakeholder1.id,

            "file_tmpi": "ttis_evaluasi/tmpi.xlsx",
            "penilaian_kritikalitas": 3,
            "analisis_ancaman": 3,
            "orang_proses_teknologi": 3,
            "lingkungan_kontrol": 3,
            "penilaian_kematangan": 3,
            "total_fase_1": 3,
            "identifikasi_respon": 3,
            "penyelidikan": 3,
            "aksi": 3,
            "pemulihan": 3,
            "total_fase_2": 3,
            "identifikasi_tindak_lanjut": 3,
            "pelaporan_review": 3,
            "pembelajaran": 3,
            "pembaruan_informasi": 3,
            "analisis_tren": 3,
            "total_fase_3": 3,
            "nilai_akhir": 3,
        })

        self.assertTrue(form.is_valid())

    def test_tmpi_form_no_data(self):
        form = TmpiForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)