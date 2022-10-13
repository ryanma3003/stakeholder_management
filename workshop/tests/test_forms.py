from django.test import TestCase
from workshop.forms import WorkshopForm
from django.utils import timezone

# Create your tests here.
class TestForms(TestCase):

    def test_workshop_form_valid_data(self):
        form = WorkshopForm(data={
            "nama":"Workshop",
            "tanggal":timezone.now(),
            "lokasi":"Jakarta",
            "deskripsi":"lorem ipsum",
            "image":"workshop/image.png",
            "jenis":"WS"
        })

        self.assertTrue(form.is_valid())

    def test_se_form_no_data(self):
        form = WorkshopForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)