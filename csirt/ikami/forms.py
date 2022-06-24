from django import forms
from .models import Ikami

class IkamiForm(forms.ModelForm):
        
    def __init__(self, *args, **kwargs):
        super(IkamiForm, self).__init__(*args, **kwargs)
        self.fields['stakeholder'].empty_label = 'Please Select'
        self.fields['month'].empty_label = 'Please Select'

    error_css_class = 'is-invalid'

    class Meta:
        model = Ikami
        
        fields = [
                'stakeholder',
                'month',
                'year',

                'tata_kelola',
                'pengelolaan_risiko',
                'kerangka_kerja',
                'pengelolaan_aset',
                'teknologi_keamanan',

                'keterlibatan_pihak_ketiga',
                'layanan_infrastruktur_awan',
                'data_pribadi'
            ]

        labels = {
            'month': 'Periode',
            'year': 'Tahun',
        }

        widgets = {
            'stakeholder': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
            'month': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
            'year': forms.TextInput(
                attrs={
                    'class': 'form-control numberOnly',
                }
            ),

            'tata_kelola': forms.TextInput(
                attrs={
                    'class': 'form-control numberOnly',
                }
            ),
            'pengelolaan_risiko': forms.TextInput(
                attrs={
                    'class': 'form-control numberOnly'
                }
            ),
            'kerangka_kerja': forms.TextInput(
                attrs={
                    'class': 'form-control numberOnly'
                }
            ),
            'pengelolaan_aset': forms.TextInput(
                attrs={
                    'class': 'form-control numberOnly'
                }
            ),
            'teknologi_keamanan': forms.TextInput(
                attrs={
                    'class': 'form-control numberOnly'
                }
            ),

            'keterlibatan_pihak_ketiga': forms.TextInput(
                attrs={
                    'class': 'form-control numberOnly'
                }
            ),
            'layanan_infrastruktur_awan': forms.TextInput(
                attrs={
                    'class': 'form-control numberOnly'
                }
            ),
            'data_pribadi': forms.TextInput(
                attrs={
                    'class': 'form-control numberOnly'
                }
            ),
        }
