from django import forms
from .models import Csm

class CsmForm(forms.ModelForm):
        
    def __init__(self, *args, **kwargs):
        super(CsmForm, self).__init__(*args, **kwargs)
        self.fields['stakeholder'].empty_label = 'Please Select'
        self.fields['month'].empty_label = 'Please Select'

    error_css_class = 'is-invalid'

    class Meta:
        model = Csm
        
        fields = [
                'stakeholder',
                'month',
                'year',

                'kesadaran',
                'audit',
                'kontrol',
                'pemenuhan',
                'kebijakan',
                'proses',

                'manajemen_aset',
                'inventaris',
                'manajemen_risiko',
                'prioritas',
                'pelaporan_identifikasi',
                'klasifikasi',

                'jaringan',
                'aplikasi',
                'pengguna',
                'manajemen_identitas',
                'cloud',
                'data',

                'perubahan',
                'monitor',
                'peringatan',
                'pemberitahuan',
                'intelijen',
                'pelaporan_deteksi',

                'penahanan',
                'penanggulanan',
                'pemulihan',
                'kegiatan_pasca',
                'pelaporan_respon'
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

            'kesadaran': forms.TextInput(
                attrs={
                    'class': 'form-control numberAndDot'
                }
            ),
            'audit': forms.TextInput(
                attrs={
                    'class': 'form-control numberAndDot'
                }
            ),
            'kontrol': forms.TextInput(
                attrs={
                    'class': 'form-control numberAndDot'
                }
            ),
            'pemenuhan': forms.TextInput(
                attrs={
                    'class': 'form-control numberAndDot'
                }
            ),
            'kebijakan': forms.TextInput(
                attrs={
                    'class': 'form-control numberAndDot'
                }
            ),
            'proses': forms.TextInput(
                attrs={
                    'class': 'form-control numberAndDot'
                }
            ),

            
            'manajemen_aset': forms.TextInput(
                attrs={
                    'class': 'form-control numberAndDot'
                }
            ),
            'inventaris': forms.TextInput(
                attrs={
                    'class': 'form-control numberAndDot'
                }
            ),
            'manajemen_risiko': forms.TextInput(
                attrs={
                    'class': 'form-control numberAndDot'
                }
            ),
            'prioritas': forms.TextInput(
                attrs={
                    'class': 'form-control numberAndDot'
                }
            ),
            'pelaporan_identifikasi': forms.TextInput(
                attrs={
                    'class': 'form-control numberAndDot'
                }
            ),
            'klasifikasi': forms.TextInput(
                attrs={
                    'class': 'form-control numberAndDot'
                }
            ),

            
            'jaringan': forms.TextInput(
                attrs={
                    'class': 'form-control numberAndDot'
                }
            ),
            'aplikasi': forms.TextInput(
                attrs={
                    'class': 'form-control numberAndDot'
                }
            ),
            'pengguna': forms.TextInput(
                attrs={
                    'class': 'form-control numberAndDot'
                }
            ),
            'manajemen_identitas': forms.TextInput(
                attrs={
                    'class': 'form-control numberAndDot'
                }
            ),
            'cloud': forms.TextInput(
                attrs={
                    'class': 'form-control numberAndDot'
                }
            ),
            'data': forms.TextInput(
                attrs={
                    'class': 'form-control numberAndDot'
                }
            ),

            
            'perubahan': forms.TextInput(
                attrs={
                    'class': 'form-control numberAndDot'
                }
            ),
            'monitor': forms.TextInput(
                attrs={
                    'class': 'form-control numberAndDot'
                }
            ),
            'peringatan': forms.TextInput(
                attrs={
                    'class': 'form-control numberAndDot'
                }
            ),
            'pemberitahuan': forms.TextInput(
                attrs={
                    'class': 'form-control numberAndDot'
                }
            ),
            'intelijen': forms.TextInput(
                attrs={
                    'class': 'form-control numberAndDot'
                }
            ),
            'pelaporan_deteksi': forms.TextInput(
                attrs={
                    'class': 'form-control numberAndDot'
                }
            ),

            
            'penahanan': forms.TextInput(
                attrs={
                    'class': 'form-control numberAndDot'
                }
            ),
            'penanggulanan': forms.TextInput(
                attrs={
                    'class': 'form-control numberAndDot'
                }
            ),
            'pemulihan': forms.TextInput(
                attrs={
                    'class': 'form-control numberAndDot'
                }
            ),
            'kegiatan_pasca': forms.TextInput(
                attrs={
                    'class': 'form-control numberAndDot'
                }
            ),
            'pelaporan_respon': forms.TextInput(
                attrs={
                    'class': 'form-control numberAndDot'
                }
            ),
        }
