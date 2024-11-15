from django.test import TestCase
from workshop.models import Workshop
from django.utils import timezone

# Create your tests here.
class TestModels(TestCase):

    def test_workshop_model(self):
        Workshop.objects.create(
            nama="Workshop",
            tanggal=timezone.now(),
            lokasi="Jakarta",
            deskripsi="lorem ipsum",
            jenis="WS",
            image="workshop/image.png"
        )

        self.assertEqual(Workshop.objects.count(), 1)