from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Workshop(models.Model):

    LEVEL_CHOICES = [
        ('bsc', 'Basic'),
        ('int', 'Intermediate'),
        ('adv', 'Advance'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    nama = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, editable=False)
    tanggal = models.DateTimeField(blank=True, null=True)
    lokasi = models.CharField(max_length=255, blank=True, null=True)
    deskripsi = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='workshop', blank=True, null=True)
    level = models.CharField(max_length=3, choices=LEVEL_CHOICES, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nama)
        super(Workshop, self).save()

    def __str__(self):
        return "{}".format(self.nama)

    def get_absolute_url(self):
        url_reverse = {
            'pk': self.id,
        }
        return reverse('workshop:detail', kwargs=url_reverse)