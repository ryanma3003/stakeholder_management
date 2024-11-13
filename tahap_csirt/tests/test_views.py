from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from tahap_csirt.views import *
from tahap_csirt.models import *
from tmpi.models import Tmpi
from compro.models import Stakeholder
from month.models import Month
from phrasalword.models import Phrasalword
from phrasalword.views import decrypt as decrypt_aes

from django.utils import timezone

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_superuser(username='d441')
        self.user.set_password('csirtd441')
        self.user.save()

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
        
        self.phrasalword = Phrasalword.objects.create(
            passphrase=b'lyAWZz4u+fppJv2sKh40If9GmVGgzUk5a1emk4roh/7kSLMxWLPtIA==',
            jabatan="Analis",
            unit_kerja="Direktorat KSSI",
            golongan="IIIa",
            user_id=self.user.id,
        )

        self.tmpi = Tmpi.objects.create(
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

        self.ttis_edukasi_create_url = '%s?s_id=%s' % (reverse('ttis:edu_create'), self.stakeholder1.id)
        self.ttis_perencanaan_create_url = '%s?s_id=%s' % (reverse('ttis:prn_create'), self.stakeholder1.id)
        self.ttis_penerapan_create_url = '%s?s_id=%s' % (reverse('ttis:pnr_create'), self.stakeholder1.id)
        self.ttis_penguatan_create_url = '%s?s_id=%s' % (reverse('ttis:png_create'), self.stakeholder1.id)
        self.ttis_evaluasi_create_url = '%s?s_id=%s' % (reverse('ttis:eva_create'), self.stakeholder1.id)
        self.ttis_pdf_view_url = '%s?s_id=%s' % (reverse('ttis:pnr_show', kwargs={'show_id':self.stakeholder1.id}), self.stakeholder1.id)

    def test_ttis_edu_create_POST_adds_new_edu(self):
        response = self.client.post(self.ttis_edukasi_create_url, {
            "stakeholder": self.stakeholder1.id,
            "sosialisasi": 1,
            "tempat": "Jakarta",
            "tanggal": timezone.now()
        })
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Edukasi.objects.filter(stakeholder_id=self.stakeholder1.id).count(), 1)

    def test_ttis_edu_delete_DELETE_deletes_edu(self):
        edu_delete = Edukasi.objects.create(
            stakeholder= self.stakeholder1,
            sosialisasi= 1,
            tempat= "Jakarta",
            tanggal= timezone.now()
        )

        url = '%s?s_id=%s' % (reverse('ttis:edu_delete', kwargs={'pk':edu_delete.stakeholder_id}), self.stakeholder1.id)

        response = self.client.delete(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Edukasi.objects.count(), 0)

    def test_ttis_prn_create_POST_adds_new_prn(self):
        response = self.client.post(self.ttis_perencanaan_create_url, {
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
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Perencanaan.objects.filter(stakeholder_id=self.stakeholder1.id).count(), 1)

    def test_ttis_prn_delete_DELETE_deletes_prn(self):
        prn_delete = Perencanaan.objects.create(
            stakeholder= self.stakeholder1,
            draft_sk= 1,
            no_draft_sk= "pwk/28",
            tgl_draft_sk= timezone.now(),
            
            draft_rfc= 1,
            no_draft_rfc= "pwk/28",
            tgl_draft_rfc= timezone.now(),

            draft_sumber_daya= 1,
            no_draft_sumber_daya= "pwk/28",
            tgl_draft_sumber_daya= timezone.now(),
        )

        url = '%s?s_id=%s' % (reverse('ttis:prn_delete', kwargs={'pk':prn_delete.stakeholder_id}), self.stakeholder1.id)

        response = self.client.delete(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Perencanaan.objects.count(), 0)

    def test_ttis_pnr_create_POST_adds_new_pnr(self):

        response = self.client.post(self.ttis_penerapan_create_url, {
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

            "file_sk": "ttis_penerapan/test.pdf",
            "file_rfc": "ttis_penerapan/test.pdf",
            "file_registrasi": "ttis_penerapan/test.pdf",
            "file_sumber_daya": "ttis_penerapan/test.pdf",
        })
        
        # use 0 because in view this function run on commit false
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Penerapan.objects.filter(stakeholder_id=self.stakeholder1.id).count(), 1)
        
    def test_ttis_pnr_pdf_view(self):
        Penerapan.objects.create(
            stakeholder= self.stakeholder1,
            doc_sk= 1,
            no_doc_sk= "pwk/28",
            tgl_doc_sk= timezone.now(),
            
            doc_rfc= 1,
            no_doc_rfc= "pwk/28",
            tgl_doc_rfc= timezone.now(),

            doc_sumber_daya= 1,
            no_doc_sumber_daya= "pwk/28",
            tgl_doc_sumber_daya= timezone.now(),

            doc_registrasi= 1,
            no_doc_registrasi= "pwk/28",
            tgl_doc_registrasi= timezone.now(),

            portal_csirt= 1,
            portal_csirt_url= "asdasd.com",

            file_sk= "ttis_penerapan/test2.pdf",
            file_rfc= "ttis_penerapan/test2.pdf",
            file_registrasi= "ttis_penerapan/test.pdf",
            file_sumber_daya= "ttis_penerapan/test.pdf",
        )

        response = self.client.post(self.ttis_pdf_view_url, {
            'passphrase': 'Mozart#30',
            'file': 'sk'
        })
        self.assertEqual(response.status_code, 200)

    def test_ttis_pnr_delete_DELETE_deletes_pnr(self):
        pnr_delete = Penerapan.objects.create(
            stakeholder= self.stakeholder1,
            doc_sk= 1,
            no_doc_sk= "pwk/28",
            tgl_doc_sk= timezone.now(),
            
            doc_rfc= 1,
            no_doc_rfc= "pwk/28",
            tgl_doc_rfc= timezone.now(),

            doc_sumber_daya= 1,
            no_doc_sumber_daya= "pwk/28",
            tgl_doc_sumber_daya= timezone.now(),

            doc_registrasi= 1,
            no_doc_registrasi= "pwk/28",
            tgl_doc_registrasi= timezone.now(),

            portal_csirt= 1,
            portal_csirt_url= "asdasd.com",

            file_sk= "ttis_penerapan/file.pdf",
            file_rfc= "ttis_penerapan/file.pdf",
            file_registrasi= "ttis_penerapan/file.pdf",
            file_sumber_daya= "ttis_penerapan/file.pdf",
        )

        url = '%s?s_id=%s' % (reverse('ttis:pnr_delete', kwargs={'pk':pnr_delete.stakeholder_id}), self.stakeholder1.id)

        response = self.client.delete(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Perencanaan.objects.count(), 0)

    def test_ttis_png_create_POST_adds_new_png(self):
        response = self.client.post(self.ttis_penguatan_create_url, {
            "stakeholder": self.stakeholder1.id,
            "status": 1,
        })
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Penguatan.objects.filter(stakeholder_id=self.stakeholder1.id).count(), 1)

    def test_ttis_png_delete_DELETE_deletes_png(self):
        png_delete = Penguatan.objects.create(
            stakeholder= self.stakeholder1,
            status= 1,
        )

        url = '%s?s_id=%s' % (reverse('ttis:png_delete', kwargs={'pk':png_delete.stakeholder_id}), self.stakeholder1.id)

        response = self.client.delete(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Penguatan.objects.count(), 0)

    def test_ttis_eva_create_POST_adds_new_eva(self):

        response = self.client.post(self.ttis_evaluasi_create_url, {
            "stakeholder": self.stakeholder1.id,
            "status": 1,
            "tmpi_id": self.tmpi.id
        })
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Evaluasi.objects.filter(stakeholder_id=self.stakeholder1.id).count(), 1)

    def test_ttis_eva_delete_DELETE_deletes_eva(self):
        eva_delete = Evaluasi.objects.create(
            stakeholder= self.stakeholder1,
            status= 1,
            tmpi_id= self.tmpi.id
        )

        url = '%s?s_id=%s' % (reverse('ttis:eva_delete', kwargs={'pk':eva_delete.stakeholder_id}), self.stakeholder1.id)

        response = self.client.delete(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Evaluasi.objects.count(), 0)