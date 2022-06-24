from django.contrib import admin

# Register your models here.
from .models import Stakeholder, Sdm, Sistemelektronik, Prosedur, ListWorkshop

class StakeholderAdmin(admin.ModelAdmin):
    readonly_fields =['slug',]

admin.site.register(Stakeholder, StakeholderAdmin)
admin.site.register(Sdm)
admin.site.register(Sistemelektronik)
admin.site.register(Prosedur)
admin.site.register(ListWorkshop)