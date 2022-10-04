from django.db import models
from django.urls import reverse

# Create your models here.
class Edukasi(models.Model):
    
    STATUS_CHOICES = [
        (1, 'Yes'),
        (0, 'No'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stakeholder = models.OneToOneField(
        'compro.Stakeholder',
        on_delete=models.CASCADE,
        primary_key=True,
    )

    sosialisasi = models.IntegerField(choices=STATUS_CHOICES, default=0)
    tempat = models.CharField(max_length=250, null=True, blank=True)
    tanggal = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.stakeholder)

    def get_absolute_url(self):
        url_reverse = {
            'pk': self.stakeholder_id,
        }
        return reverse('stakeholder:detail', kwargs=url_reverse)

class Perencanaan(models.Model):
    
    STATUS_CHOICES = [
        (1, 'Yes'),
        (0, 'No'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stakeholder = models.OneToOneField(
        'compro.Stakeholder',
        on_delete=models.CASCADE,
        primary_key=True,
    )

    draft_sk = models.IntegerField(choices=STATUS_CHOICES, default=0)
    no_draft_sk = models.CharField(max_length=250, null=True, blank=True)
    tgl_draft_sk = models.DateTimeField(null=True, blank=True)
    
    draft_rfc = models.IntegerField(choices=STATUS_CHOICES, default=0)
    no_draft_rfc = models.CharField(max_length=250, null=True, blank=True)
    tgl_draft_rfc = models.DateTimeField(null=True, blank=True)

    draft_sumber_daya = models.IntegerField(choices=STATUS_CHOICES, default=0)
    no_draft_sumber_daya = models.CharField(max_length=250, null=True, blank=True)
    tgl_draft_sumber_daya = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.stakeholder)

    def get_absolute_url(self):
        url_reverse = {
            'pk': self.stakeholder_id,
        }
        return reverse('stakeholder:detail', kwargs=url_reverse)

class Penerapan(models.Model):
    
    STATUS_CHOICES = [
        (1, 'Yes'),
        (0, 'No'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stakeholder = models.OneToOneField(
        'compro.Stakeholder',
        on_delete=models.CASCADE,
        primary_key=True,
    )

    doc_sk = models.IntegerField(choices=STATUS_CHOICES, default=0)
    no_doc_sk = models.CharField(max_length=250, null=True, blank=True)
    tgl_doc_sk = models.DateTimeField(null=True, blank=True)
    file_sk = models.FileField(upload_to='ttis_penerapan', null=True, blank=True)

    doc_rfc = models.IntegerField(choices=STATUS_CHOICES, default=0)
    no_doc_rfc = models.CharField(max_length=250, null=True, blank=True)
    tgl_doc_rfc = models.DateTimeField(null=True, blank=True)
    file_rfc = models.FileField(upload_to='ttis_penerapan', null=True, blank=True)

    doc_sumber_daya = models.IntegerField(choices=STATUS_CHOICES, default=0)
    no_doc_sumber_daya = models.CharField(max_length=250, null=True, blank=True)
    tgl_doc_sumber_daya = models.DateTimeField(null=True, blank=True)
    file_sumber_daya = models.FileField(upload_to='ttis_penerapan', null=True, blank=True)

    doc_registrasi = models.IntegerField(choices=STATUS_CHOICES, default=0)
    no_doc_registrasi = models.CharField(max_length=250, null=True, blank=True)
    tgl_doc_registrasi = models.DateTimeField(null=True, blank=True)
    file_registrasi = models.FileField(upload_to='ttis_penerapan', null=True, blank=True)

    portal_csirt = models.IntegerField(choices=STATUS_CHOICES)
    portal_csirt_url = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.stakeholder)

    def get_absolute_url(self):
        url_reverse = {
            'pk': self.stakeholder_id,
        }
        return reverse('stakeholder:detail', kwargs=url_reverse)

class Penguatan(models.Model):
    
    STATUS_CHOICES = [
        (1, 'Yes'),
        (0, 'No'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stakeholder = models.OneToOneField(
        'compro.Stakeholder',
        on_delete=models.CASCADE,
        primary_key=True,
    )

    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    def __str__(self):
        return "{}".format(self.stakeholder)

    def get_absolute_url(self):
        url_reverse = {
            'pk': self.stakeholder_id,
        }
        return reverse('stakeholder:detail', kwargs=url_reverse)

class Evaluasi(models.Model):
    
    STATUS_CHOICES = [
        (1, 'Yes'),
        (0, 'No'),
    ]
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stakeholder = models.OneToOneField(
        'compro.Stakeholder',
        on_delete=models.CASCADE,
        primary_key=True,
    )

    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    tmpi = models.ForeignKey('tmpi.Tmpi', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.stakeholder)

    def get_absolute_url(self):
        url_reverse = {
            'pk': self.stakeholder_id,
        }
        return reverse('stakeholder:detail', kwargs=url_reverse)