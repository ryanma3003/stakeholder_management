from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from phrasalword.views import *
from phrasalword.models import *


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_superuser(username='d441')
        self.user.set_password('csirtd441')
        self.user.save()

        self.client.login(username='d441', password='csirtd441')

        self.phrasalword = Phrasalword.objects.create(
            passphrase=b'lyAWZz4u+fppJv2sKh40If9GmVGgzUk5a1emk4roh/7kSLMxWLPtIA==',
            jabatan="Analis",
            unit_kerja="Direktorat KSSI",
            golongan="IIIa",
            user_id=self.user.id,
        )

        self.profile_show_pass_url = reverse('profile:show_pass')
        self.profile_update_url = reverse('profile:update', kwargs={'pk':self.phrasalword.user_id})

    def test_phrasalword_show_pass_GET(self):
        response = self.client.post(self.profile_show_pass_url, {
            'password': 'Mozart#30',
        })
        self.assertEqual(response.status_code, 200)

    def test_phrasalword_update_GET(self):
        response = self.client.get(self.profile_update_url)
        self.assertEqual(response.status_code, 200)