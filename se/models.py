from django.db import models
from django.urls import reverse
from .validators import validate_indeks_nilai

# Create your models here.

class Se(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stakeholder = models.ForeignKey('compro.Stakeholder', on_delete=models.CASCADE)
    month = models.ForeignKey('month.Month', on_delete=models.CASCADE, blank=True)
    year = models.IntegerField()
    indeks_nilai = models.FloatField(blank=True, validators=[validate_indeks_nilai])
    indeks_ket = models.CharField(blank=True, max_length=255)
    sistem = models.TextField()
    keterangan = models.TextField()

    def __str__(self):
        return "{}".format(self.stakeholder)

    def get_absolute_url(self):
        url_reverse = {
            'pk': self.id,
        }
        return reverse('se:detail', kwargs=url_reverse)