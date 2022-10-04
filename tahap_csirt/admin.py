from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Edukasi)
admin.site.register(Perencanaan)
admin.site.register(Penerapan)
admin.site.register(Penguatan)
admin.site.register(Evaluasi)