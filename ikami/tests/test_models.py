from django.test import TestCase
from ikami.models import Ikami
from month.models import Month
from compro.models import Stakeholder

# Create your tests here.
class TestModels(TestCase):
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

    def test_ikami_model(self):
        Ikami.objects.create(
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

        self.assertEqual(Ikami.objects.count(), 1)