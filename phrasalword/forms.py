from django import forms
from .models import Phrasalword
# from django.core.validators import RegexValidator

class PhrasalwordForm(forms.ModelForm):
        
    def __init__(self, *args, **kwargs):
        super(PhrasalwordForm, self).__init__(*args, **kwargs)
        # self.fields['passphrase'].help_text = 'Use strong passphrase with combination letter, number, and symbol.'
        # self.fields['passphrase'].validators = RegexValidator(r"^[a-zA-Z0-9]+$", "Your string should contain letter A in it.")

    error_css_class = 'is-invalid'

    class Meta:
        model = Phrasalword

        exclude = ['user']
        
        fields = [
                # 'passphrase',
                'unit_kerja',
                'jabatan',
                'golongan'
            ]

        labels = {
            'unit_kerja': 'Unit Kerja',
        }

        widgets = {
            # 'passphrase': forms.PasswordInput(
            #     attrs={
            #         'class': 'form-control'
            #     }
            # ),
            'unit_kerja': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'jabatan': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'golongan': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
        }

