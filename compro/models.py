from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Stakeholder(models.Model):
    
    INDUSTRI = 'IN'
    KONSTRUKSI = 'KN'
    KAMSIBER = 'KM'
    
    FIELD_CHOICES = [
        (INDUSTRI, 'Industri'),
        (KONSTRUKSI, 'Konstruksi'),
        (KAMSIBER, 'Kamsiber'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='stakeholder_logo', blank=True, null=True)
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(blank=True, editable=False)
    type = models.CharField(max_length=255)
    field = models.CharField(max_length=5, choices=FIELD_CHOICES)
    address = models.TextField()
    info = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, default='info@corporate.com')
    landing_page = models.CharField(max_length=255, blank=True, null=True)
    kode_pos = models.CharField(max_length=10, blank=True, null=True)
    pic = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Stakeholder, self).save()

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        url_reverse = {
            'pk': self.id,
        }
        return reverse('stakeholder:detail', kwargs=url_reverse)


class Sdm(models.Model):
    GENDER_CHOICES = [
        ('m', 'Laki-laki'),
        ('f', 'Perempuan'),
    ]

    CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stakeholder = models.ForeignKey('Stakeholder', on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    jabatan = models.CharField( max_length=255, blank=True, null=True)
    unit_kerja = models.CharField(max_length=255, blank=True, null=True)
    kompetensi = models.TextField(blank=True, null=True)
    sertifikat = models.TextField(blank=True, null=True)
    telepon = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, default='info@corporate.com')
    csirt = models.CharField(max_length=5, choices=CHOICES, default='no')
    narahubung = models.CharField(max_length=5, choices=CHOICES, default='no')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return "{}".format(self.nama)

    def get_absolute_url(self):
        url_reverse = {
            'pk': self.stakeholder_id,
        }
        return reverse('stakeholder:detail', kwargs=url_reverse)


class Sistemelektronik(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stakeholder = models.ForeignKey('Stakeholder', on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    spesifikasi = models.TextField(blank=True, null=True)
    unit = models.CharField(max_length=255, blank=True, null=True)
    unit_pengelola = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.nama)

    def get_absolute_url(self):
        url_reverse = {
            'pk': self.stakeholder_id,
        }
        return reverse('stakeholder:detail', kwargs=url_reverse)



class Prosedur(models.Model):
    RELEASE = 'RL'
    PUBLICATION = 'PB'
    DRAFT = 'DR'
    
    STATUS_CHOICES = [
        (RELEASE, 'Release'),
        (PUBLICATION, 'Publication'),
        (DRAFT, 'Draft'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stakeholder = models.ForeignKey('Stakeholder', on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    nomer = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=DRAFT)
    tahun = models.CharField(max_length=4, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.nama)

    def get_absolute_url(self):
        url_reverse = {
            'pk': self.stakeholder_id,
        }
        return reverse('stakeholder:detail', kwargs=url_reverse)

class ListWorkshop(models.Model):
    PESERTA = 'PS'
    NARASUMBER = 'NS'
    
    STATUS_CHOICES = [
        (PESERTA, 'Peserta'),
        (NARASUMBER, 'Narasumber'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stakeholder = models.ForeignKey('Stakeholder', on_delete=models.CASCADE)
    sdm = models.ForeignKey('Sdm', on_delete=models.CASCADE, null=True, blank=True)
    workshop = models.ForeignKey('workshop.Workshop', on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.stakeholder)

    def get_absolute_url(self):
        url_reverse = {
            'pk': self.stakeholder_id,
        }
        return reverse('stakeholder:detail', kwargs=url_reverse)