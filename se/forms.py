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

        exclude = ['indeks_ket']
        
        fields = [
                'stakeholder',
                'month',
                'year',
                'indeks_nilai',
                'sistem',
                'keterangan'
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
