from django.test import TestCase
from tahap_csirt.models import *
from compro.models import Stakeholder
from month.models import Month
from tmpi.models import Tmpi
from django.utils import timezone

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
            field="IN",
            address="test",
            info="test",
            phone="01812812",
            email="asd@adsa.com",
            landing_page="",
            kode_pos="12312"
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

    def test_edukasi_model(self):
        Edukasi.objects.create(
            stakeholder= self.stakeholder1,
            sosialisasi= 1,
            tempat= "Jakarta",
            tanggal= timezone.now()
        )

        self.assertEqual(Edukasi.objects.count(), 1)

    def test_perencanaan_model(self):
        Perencanaan.objects.create(
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

        self.assertEqual(Perencanaan.objects.count(), 1)

    def test_penerapan_model(self):
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

        self.assertEqual(Penerapan.objects.count(), 1)

    def test_penguatan_model(self):
        Penguatan.objects.create(
            stakeholder= self.stakeholder1,
            status= 1,
        )

        self.assertEqual(Penguatan.objects.count(), 1)

    def test_evaluasi_model(self):
        Evaluasi.objects.create(
            stakeholder= self.stakeholder1,
            status= 1,
            tmpi_id= self.tmpi.id
        )

        self.assertEqual(Evaluasi.objects.count(), 1)