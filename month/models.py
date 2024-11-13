from django.db import models

# Create your models here.
class Month(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    month_id = models.CharField(blank=True, max_length=255)
    month_en = models.CharField(blank=True, max_length=255)
    month_abb = models.CharField(blank=True, max_length=255)
    
    def save(self, *args, **kwargs):
        super(Month, self).save()

    def __str__(self):
        return "{}".format(self.month_abb)