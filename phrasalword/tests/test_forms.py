from django.test import TestCase, Client
from phrasalword.forms import PhrasalwordForm
from django.contrib.auth.models import User

# Create your tests here.
class TestForms(TestCase):
    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_superuser(
            username='d441', email='d441@bssn.go.id', password='my_secret')
        
        self.client.login(username='d441', password='csirtd441')

    def test_se_form_valid_data(self):
        form = PhrasalwordForm(data={
            "passphrase":b'lyAWZz4u+fppJv2sKh40If9GmVGgzUk5a1emk4roh/7kSLMxWLPtIA==',
            "jabatan":"analis",
            "unit_kerja":"Direktorat KSSI",
            "golongan":"IIIa",
            "user_id":self.user.id,
        })

        self.assertTrue(form.is_valid())

    def test_se_form_no_data(self):
        form = PhrasalwordForm(data={})

        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors), 0)