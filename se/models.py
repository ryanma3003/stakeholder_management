from django.db import models
from django.urls import reverse
from .validators import validate_indeks_nilai

# Create your models here.

class Se(models.Model):
    STATUS_CHOICES = [
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stakeholder = models.ForeignKey('compro.Stakeholder', on_delete=models.CASCADE)
    month = models.ForeignKey('month.Month', on_delete=models.CASCADE, blank=True)
    year = models.IntegerField()
    indeks_nilai = models.FloatField(blank=True, validators=[validate_indeks_nilai])
    indeks_ket = models.CharField(blank=True, max_length=255)
    sistem = models.TextField()
    keterangan = models.TextField()

    jenis_usaha = models.CharField(blank=True, max_length=255)
    
    nilai_investasi = models.CharField(blank=True, max_length=1, choices=STATUS_CHOICES)
    bobot_nilai_investasi = models.CharField(max_length=3, default=0)
    total_anggaran = models.CharField(blank=True, max_length=1, choices=STATUS_CHOICES)
    bobot_total_anggaran = models.CharField(max_length=3, default=0)
    kewajiban = models.CharField(blank=True, max_length=1, choices=STATUS_CHOICES)
    bobot_kewajiban = models.CharField(max_length=3, default=0)
    kriptografi = models.CharField(blank=True, max_length=1, choices=STATUS_CHOICES)
    bobot_kriptografi = models.CharField(max_length=3, default=0)
    pengguna = models.CharField(blank=True, max_length=1, choices=STATUS_CHOICES)
    bobot_pengguna = models.CharField(max_length=3, default=0)
    data_pribadi = models.CharField(blank=True, max_length=1, choices=STATUS_CHOICES)
    bobot_data_pribadi = models.CharField(max_length=3, default=0)
    kritis_data = models.CharField(blank=True, max_length=1, choices=STATUS_CHOICES)
    bobot_kritis_data = models.CharField(max_length=3, default=0)
    kritis_proses = models.CharField(blank=True, max_length=1, choices=STATUS_CHOICES)
    bobot_kritis_proses = models.CharField(max_length=3, default=0)
    dampak_kegagalan = models.CharField(blank=True, max_length=1, choices=STATUS_CHOICES)
    bobot_dampak_kegagalan = models.CharField(max_length=3, default=0)
    potensi_kerugian = models.CharField(blank=True, max_length=1, choices=STATUS_CHOICES)
    bobot_potensi_kerugian = models.CharField(max_length=3, default=0)


    def __str__(self):
        return "{}".format(self.stakeholder)

    def get_absolute_url(self):
        url_reverse = {
            'pk': self.id,
        }
        return reverse('se:detail', kwargs=url_reverse)