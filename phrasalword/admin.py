from django.contrib import admin

# Register your models here.
from .models import *

class PhrasalwordAdmin(admin.ModelAdmin):
    readonly_fields =['passphrase',]

admin.site.register(Phrasalword, PhrasalwordAdmin)