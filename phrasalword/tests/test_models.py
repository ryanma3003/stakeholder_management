from django.test import TestCase, Client
from phrasalword.models import Phrasalword
from django.contrib.auth.models import User

# Create your tests here.
class TestModels(TestCase):
    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_superuser(
            username='d441', email='d441@bssn.go.id', password='my_secret')
        
        self.client.login(username='d441', password='csirtd441')

    def test_ikami_model(self):
        Phrasalword.objects.create(
            passphrase=b'lyAWZz4u+fppJv2sKh40If9GmVGgzUk5a1emk4roh/7kSLMxWLPtIA==',
            jabatan="Analis",
            unit_kerja="Direktorat KSSI",
            golongan="IIIa",
            user_id=self.user.id,
        )

        self.assertEqual(Phrasalword.objects.count(), 1)