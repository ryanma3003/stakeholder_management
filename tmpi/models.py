from django.db import models
from django.urls import reverse
from django.conf import settings
import os

# Create your models here.
class Tmpi(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stakeholder = models.ForeignKey('compro.Stakeholder', on_delete=models.CASCADE)
    month = models.ForeignKey('month.Month', on_delete=models.CASCADE)
    year = models.IntegerField()

    file_tmpi = models.FileField(upload_to='ttis_evaluasi', blank=True, null=True)

    penilaian_kritikalitas = models.FloatField()
    analisis_ancaman = models.FloatField()
    orang_proses_teknologi = models.FloatField()
    lingkungan_kontrol = models.FloatField()
    penilaian_kematangan = models.FloatField()
    total_fase_1 = models.FloatField()

    identifikasi_respon = models.FloatField()
    penyelidikan = models.FloatField()
    aksi = models.FloatField()
    pemulihan = models.FloatField()
    total_fase_2 = models.FloatField()

    identifikasi_tindak_lanjut = models.FloatField()
    pelaporan_review = models.FloatField()
    pembelajaran = models.FloatField()
    pembaruan_informasi = models.FloatField()
    analisis_tren = models.FloatField()
    total_fase_3 = models.FloatField()

    nilai_akhir = models.FloatField()

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )

    @property
    def filename(self):
        return os.path.basename(self.file_tmpi.name)

    def __str__(self):
        return "{}".format(self.stakeholder)

    def get_absolute_url(self):
        url_reverse = {
            'pk': self.id,
        }
        return reverse('tmpi:detail', kwargs=url_reverse)