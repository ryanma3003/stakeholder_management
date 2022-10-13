from django import forms
from .models import Tmpi
from django.core.exceptions import ValidationError

class TmpiForm(forms.ModelForm):

    def clean_file_tmpi(self):
        file_tmpi = self.cleaned_data.get('file_tmpi', False)
        if file_tmpi:
            if file_tmpi.name.lower().endswith(('.xlsx')) :
                if file_tmpi.size > 1*1024*1024:
                    raise ValidationError("File too large ( > 1mb )")
                return file_tmpi
            else :
                raise ValidationError("Not .xlsx format")

    file_tmpi = forms.FileField(
        label = 'TMPI Excel (.xlsx)',
        help_text = 'Please use underscore not space in file name and max size 1 megabytes',
        required = False,
        widget = forms.FileInput(
            attrs={
                'class' : 'form-file-input form-control',
                'type' : 'file',
            }
        )
    )
        
    def __init__(self, *args, **kwargs):
        super(TmpiForm, self).__init__(*args, **kwargs)
        self.fields['stakeholder'].empty_label = 'Please Select'
        self.fields['month'].empty_label = 'Please Select'

    error_css_class = 'is-invalid'

    class Meta:
        model = Tmpi
        
        fields = [
                'stakeholder',
                'month',
                'year',
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

            
        }
