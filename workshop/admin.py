from django.contrib import admin

# Register your models here.
from .models import Workshop

class WorkshopAdmin(admin.ModelAdmin):
    readonly_fields =['slug',]

admin.site.register(Workshop, WorkshopAdmin)