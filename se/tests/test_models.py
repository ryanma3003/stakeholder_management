from django.test import TestCase
from se.models import Se
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

    def test_se_model(self):
        Se.objects.create(
            year=2022,
            indeks_nilai=36.0,
            indeks_ket="Tinggi",
            sistem="test",
            keterangan="test",
            month=self.month1,
            stakeholder=self.stakeholder1,
        )

        self.assertEqual(Se.objects.count(), 1)