from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Ikami(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stakeholder = models.ForeignKey('compro.Stakeholder', on_delete=models.CASCADE)
    month = models.ForeignKey('month.Month', on_delete=models.CASCADE)
    year = models.IntegerField()

    tata_kelola = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(126)])
    pengelolaan_risiko = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(72)])
    kerangka_kerja = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(159)])
    pengelolaan_aset = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(168)])
    teknologi_keamanan = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(120)])

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