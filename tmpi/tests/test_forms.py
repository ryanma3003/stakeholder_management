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
            field="Manufaktur",
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
            "indeks_nilai": 36.0,
            "indeks_ket": "Tinggi",
            "sistem": "test",
            "keterangan": "test",
            "month": self.month1.id,
            "stakeholder": self.stakeholder1.id,
        })

        self.assertTrue(form.is_valid())

    def test_se_form_no_data(self):
        form = SeForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)