from django.db import models
from django.urls import reverse

# Create your models here.
class Csm(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stakeholder = models.ForeignKey('compro.Stakeholder', on_delete=models.CASCADE)
    month = models.ForeignKey('month.Month', on_delete=models.CASCADE)
    year = models.IntegerField()

    kesadaran = models.FloatField()
    audit = models.FloatField()
    kontrol = models.FloatField()
    pemenuhan = models.FloatField()
    kebijakan = models.FloatField()
    proses = models.FloatField()

    manajemen_aset = models.FloatField()
    inventaris = models.FloatField()
    manajemen_risiko = models.FloatField()
    prioritas = models.FloatField()
    pelaporan_identifikasi = models.FloatField()
    klasifikasi = models.FloatField()

    jaringan = models.FloatField()
    aplikasi = models.FloatField()
    pengguna = models.FloatField()
    manajemen_identitas = models.FloatField()
    cloud = models.FloatField()
    data = models.FloatField()

    perubahan = models.FloatField()
    monitor = models.FloatField()
    peringatan = models.FloatField()
    pemberitahuan = models.FloatField()
    intelijen = models.FloatField()
    pelaporan_deteksi = models.FloatField()

    penahanan = models.FloatField()
    penanggulanan = models.FloatField()
    pemulihan = models.FloatField()
    kegiatan_pasca = models.FloatField()
    pelaporan_respon = models.FloatField()

    def __str__(self):
        return "{}".format(self.stakeholder)

    def get_absolute_url(self):
        url_reverse = {
            'pk': self.id,
        }
        return reverse('csm:detail', kwargs=url_reverse)