from django import forms
from .models import Se
from month.models import Month
from compro.models import Stakeholder

class SeForm(forms.ModelForm):
        
    def __init__(self, *args, **kwargs):
        super(SeForm, self).__init__(*args, **kwargs)
        self.fields['stakeholder'].empty_label = 'Please Select'
        self.fields['month'].empty_label = 'Please Select'

    error_css_class = 'is-invalid'

    class Meta:
        model = Se

        exclude = ['indeks_ket', 'indeks_nilai']
        
        fields = [
                'stakeholder',
                'month',
                'year',
                'jenis_usaha',
                'sistem',
                'keterangan',
                
                'nilai_investasi',
                'total_anggaran',
                'kewajiban',
                'kriptografi',
                'pengguna',
                'data_pribadi',
                'kritis_data',
                'kritis_proses',
                'dampak_kegagalan',
                'potensi_kerugian',
                
                'bobot_nilai_investasi',
                'bobot_total_anggaran',
                'bobot_kewajiban',
                'bobot_kriptografi',
                'bobot_pengguna',
                'bobot_data_pribadi',
                'bobot_kritis_data',
                'bobot_kritis_proses',
                'bobot_dampak_kegagalan',
                'bobot_potensi_kerugian'
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
            'jenis_usaha': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'indeks_nilai': forms.TextInput(
                attrs={
                    'class': 'form-control numberAndDot'
                }
            ),
            'sistem': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'keterangan': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),

            'jenis_usaha': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nilai_investasi': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
            'bobot_nilai_investasi': forms.HiddenInput(),
            'total_anggaran': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
            'bobot_total_anggaran': forms.HiddenInput(),
            'kewajiban': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
            'bobot_kewajiban': forms.HiddenInput(),
            'kriptografi': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
            'bobot_kriptografi': forms.HiddenInput(),
            'pengguna': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
            'bobot_pengguna': forms.HiddenInput(),
            'data_pribadi': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
            'bobot_data_pribadi': forms.HiddenInput(),
            'kritis_data': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
            'bobot_kritis_data': forms.HiddenInput(),
            'kritis_proses': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
            'bobot_kritis_proses': forms.HiddenInput(),
            'dampak_kegagalan': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
            'bobot_dampak_kegagalan': forms.HiddenInput(),
            'potensi_kerugian': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
            'bobot_potensi_kerugian': forms.HiddenInput(),
        }


# class SeForm(forms.Form):
#     stakeholder = forms.ModelChoiceField(
#         queryset=Stakeholder.objects.all(), 
#         empty_label="Please Select",
#         widget=forms.Select(
#             attrs={
#                 'class': 'default-select wide form-control'
#             }
#         )
#     )

#     periode = forms.ModelChoiceField(
#         queryset=Month.objects.all(), 
#         empty_label="Please Select",
#         widget=forms.Select(
#             attrs={
#                 'class': 'default-select wide form-control'
#             }
#         )
#     )

#     year = forms.CharField(
#         label = 'Tahun',
#         max_length = 4,
#         widget = forms.TextInput(
#             attrs={
#                 'class': 'form-control numberOnly',
#             }
#         )
#     )

#     indeks_nilai = forms.FloatField(
#         label = 'Nilai Kategorisasi SE',
#         widget = forms.TextInput(
#             attrs={
#                 'class': 'form-control numberAndDot',
#             }
#         )
#     )

#     sistem = forms.CharField(
#         label = 'Sistem Elektronik',
#         widget = forms.Textarea(
#             attrs={
#                 'class': 'form-control',
#             }
#         )
#     )

#     keterangan = forms.CharField(
#         label = 'Keterangan',
#         widget = forms.Textarea(
#             attrs={
#                 'class': 'form-control',
#             }
#         )
#     )

#     def clean_year(self):
#         year_input = self.cleaned_data.get('year')

#         return year_input
