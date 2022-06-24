from django.db import models
from django.urls import reverse

# Create your models here.
class Ikami(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stakeholder = models.ForeignKey('compro.Stakeholder', on_delete=models.CASCADE)
    month = models.ForeignKey('month.Month', on_delete=models.CASCADE)
    year = models.IntegerField()

    tata_kelola = models.IntegerField()
    pengelolaan_risiko = models.IntegerField()
    kerangka_kerja = models.IntegerField()
    pengelolaan_aset = models.IntegerField()
    teknologi_keamanan = models.IntegerField()

    keterlibatan_pihak_ketiga = models.IntegerField(blank=True, null=True)
    layanan_infrastruktur_awan = models.IntegerField(blank=True, null=True)
    data_pribadi = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.stakeholder)

    def get_absolute_url(self):
        url_reverse = {
            'pk': self.id,
        }
        return reverse('ikami:detail', kwargs=url_reverse)