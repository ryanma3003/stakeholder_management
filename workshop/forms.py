from django import forms
from .models import Workshop

class WorkshopForm(forms.ModelForm):
        
    def __init__(self, *args, **kwargs):
        super(WorkshopForm, self).__init__(*args, **kwargs)

    error_css_class = 'is-invalid'

    class Meta:
        model = Workshop
        
        fields = [
                'nama',
                'tanggal',
                'lokasi',
            ]

        widgets = {
            'nama': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'tanggal': forms.DateTimeInput(
                attrs={
                    'class': 'datepicker-default form-control',
                    'id': 'datepicker'
                }
            ),
            'lokasi': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }