from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Phrasalword(models.Model):
    
    GOL_CHOICES = [
        ('IIa', 'IIa'),
        ('IIb', 'IIb'),
        ('IIc', 'IIc'),
        ('IId', 'IId'),
        ('IIIa', 'IIIa'),
        ('IIIb', 'IIIb'),
        ('IIIc', 'IIIc'),
        ('IIId', 'IIId'),
        ('IVa', 'IVa'),
        ('IVb', 'IVb'),
        ('IVc', 'IVc'),
        ('IVd', 'IVd'),
        ('IVe', 'IVe'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    passphrase = models.BinaryField(max_length=None, null=True, blank=True)
    unit_kerja = models.CharField(max_length=250, null=True, blank=True)
    jabatan = models.CharField(max_length=250, null=True, blank=True)
    golongan = models.CharField(max_length=10, choices=GOL_CHOICES, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.user.name)

    def get_absolute_url(self):
        url_reverse = {
            'pk': self.user_id,
        }
        return reverse('profile:update', kwargs=url_reverse)
