from django.test import TestCase
from csm.forms import CsmForm
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
            field="Manufaktur",
            address="test",
            info="test",
            phone="01812812",
            email="asd@adsa.com",
            landing_page="",
            kode_pos="12312"
        )

    def test_se_form_valid_data(self):
        form = CsmForm(data={
            "year": 2022,
            "kesadaran":4,
            "audit":4,
            "kontrol":3,
            "pemenuhan":3,
            "kebijakan":2,
            "proses":2,
            "manajemen_aset":3,
            "inventaris":4,
            "manajemen_risiko":3,
            "prioritas":3,
            "pelaporan_identifikasi":3,
            "klasifikasi":4,
            "jaringan":4,
            "aplikasi":4,
            "pengguna":2,
            "manajemen_identitas":4,
            "cloud":3,
            "data":4,
            "perubahan":3,
            "monitor":5,
            "peringatan":4,
            "pemberitahuan":3,
            "intelijen":3,
            "pelaporan_deteksi":4,
            "penahanan":4,
            "penanggulanan":3,
            "pemulihan":4,
            "kegiatan_pasca":3,
            "pelaporan_respon":3,
            "month": self.month1.id,
            "stakeholder": self.stakeholder1.id,
        })

        self.assertTrue(form.is_valid())

    def test_se_form_no_data(self):
        form = CsmForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 32)