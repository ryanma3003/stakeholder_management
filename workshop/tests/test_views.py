from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

from workshop.views import *


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.workshop1 = Workshop.objects.create(
            nama="Workshop",
            tanggal=timezone.now(),
            lokasi="Jakarta",
            deskripsi="lorem ipsum",
            jenis="WS",
            image="workshop/image.png"
        )

        self.workshop_list_url = reverse('workshop:index')
        self.workshop_detail_url = reverse('workshop:detail', kwargs={'pk':self.workshop1.id})
        self.workshop_create_url = reverse('workshop:create')
        self.workshop_update_url = reverse('workshop:update', kwargs={'pk':self.workshop1.id})
        self.workshop_delete_url = reverse('workshop:delete', kwargs={'pk':self.workshop1.id})

        user = User.objects.create_superuser(username='d441')
        user.set_password('csirtd441')
        user.save()

        self.client.login(username='d441', password='csirtd441')

    def test_workshop_list_GET(self):
        response = self.client.get(self.workshop_list_url)
        self.assertEquals(response.status_code, 200)

    def test_workshop_detail_GET(self):
        response = self.client.get(self.workshop_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.workshop1.nama, 'Workshop')

    def test_workshop_create_GET(self):
        response = self.client.get(self.workshop_create_url)
        self.assertEquals(response.status_code, 200)

    def test_workshop_update_GET(self):
        response = self.client.get(self.workshop_update_url)
        self.assertEquals(response.status_code, 200)

    def test_workshop_delete_DELETE_deletes_stakeholder(self):
        response = self.client.delete(self.workshop_delete_url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Workshop.objects.count(), 0)