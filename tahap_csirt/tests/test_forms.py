from django.test import TestCase, Client
from tahap_csirt.forms import *
from tmpi.models import Tmpi
from compro.models import Stakeholder
from django.contrib.auth.models import User
from month.models import Month
from django.utils import timezone

# Create your tests here.
class TestForms(TestCase):
    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_superuser(
            username='d441', email='d441@bssn.go.id', password='my_secret')
        
        self.client.login(username='d441', password='csirtd441')

        self.month1 = Month.objects.create(
            month_id="Januari",
            month_en="January",
            month_abb="Jan",
        )

        self.stakeholder1 = Stakeholder.objects.create(
            name="stakeholder1",
            type="BUMN",
            field="IN",
            address="test",
            info="test",
            phone="01812812",
            email="asd@adsa.com",
            landing_page="",
            kode_pos="12312"
        )

    def get_form_kwargs(self):
        kwargs = {'s_id': self.stakeholder1.id}
        return kwargs

    def test_edukasi_form_valid_data(self):
        form = EdukasiForm(data={
            "stakeholder": self.stakeholder1.id,
            "sosialisasi": 1,
            "tempat": "Jakarta",
            "tanggal": timezone.now()
        })

        self.assertTrue(form.is_valid())

    def test_edukasi_form_no_data(self):
        form = EdukasiForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_perencanaan_form_valid_data(self):
        form = PerencanaanForm(data={
            "stakeholder": self.stakeholder1.id,
            "draft_sk": 1,
            "no_draft_sk": "pwk/28",
            "tgl_draft_sk": timezone.now(),
            
            "draft_rfc": 1,
            "no_draft_rfc": "pwk/28",
            "tgl_draft_rfc": timezone.now(),

            "draft_sumber_daya": 1,
            "no_draft_sumber_daya": "pwk/28",
            "tgl_draft_sumber_daya": timezone.now(),
        })

        self.assertTrue(form.is_valid())

    def test_perencanaan_form_no_data(self):
        form = PerencanaanForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)

    def test_penerapan_form_valid_data(self):
        form = PenerapanForm(data={
            "stakeholder": self.stakeholder1.id,
            "doc_sk": 1,
            "no_doc_sk": "pwk/28",
            "tgl_doc_sk": timezone.now(),
            
            "doc_rfc": 1,
            "no_doc_rfc": "pwk/28",
            "tgl_doc_rfc": timezone.now(),

            "doc_sumber_daya": 1,
            "no_doc_sumber_daya": "pwk/28",
            "tgl_doc_sumber_daya": timezone.now(),

            "doc_registrasi": 1,
            "no_doc_registrasi": "pwk/28",
            "tgl_doc_registrasi": timezone.now(),

            "portal_csirt": 1,
            "portal_csirt_url": "asdasd.com",

            "file_sk": "ttis_penerapan/file.pdf",
            "file_rfc": "ttis_penerapan/file.pdf",
            "file_registrasi": "ttis_penerapan/file.pdf",
            "file_sumber_daya": "ttis_penerapan/file.pdf",
        })

        self.assertTrue(form.is_valid())

    def test_penerapan_form_no_data(self):
        form = PenerapanForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 5)

    def test_penguatan_form_valid_data(self):
        form = PenguatanForm(data={
            "stakeholder": self.stakeholder1.id,
            "status": 1,
        })

        self.assertTrue(form.is_valid())

    def test_penguatan_form_no_data(self):
        form = PenguatanForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_evaluasi_form_valid_data(self):
        tmpi = Tmpi.objects.create(
            year=2022,
            month=self.month1,
            stakeholder=self.stakeholder1,

            file_tmpi= "ttis_evaluasi/tmpi.xlsx",
            penilaian_kritikalitas= 3,
            analisis_ancaman= 3,
            orang_proses_teknologi= 3,
            lingkungan_kontrol= 3,
            penilaian_kematangan= 3,
            total_fase_1= 3,
            identifikasi_respon= 3,
            penyelidikan= 3,
            aksi= 3,
            pemulihan= 3,
            total_fase_2= 3,
            identifikasi_tindak_lanjut= 3,
            pelaporan_review= 3,
            pembelajaran= 3,
            pembaruan_informasi= 3,
            analisis_tren= 3,
            total_fase_3= 3,
            nilai_akhir= 3,
        )
        
        form = EvaluasiForm(data={
            "stakeholder": self.stakeholder1.id,
            "status": 1,
            "tmpi_id": tmpi.id
        })

        self.assertTrue(form.is_valid())

    def test_evaluasi_form_no_data(self):
        form = EvaluasiForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)