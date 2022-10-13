from django import forms
from .models import Stakeholder, Sdm, Sistemelektronik, Prosedur, ListWorkshop
from django.core.exceptions import ValidationError

class ComproForm(forms.ModelForm):

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.name.lower().endswith(('.png', '.jpg', '.jpeg')) :
                if image.size > 0.5*1024*1024:
                    raise ValidationError("Image file too large ( > 500kb )")
                return image
            else :
                raise ValidationError("File is not an image.")

    image = forms.FileField(
        label = 'Stakeholder Logo',
        required = False,
        help_text = 'Please use format .png, .jpg, or .jpeg and max. 500 kilobytes',
        widget = forms.FileInput(
            attrs={
                'class' : 'form-file-input form-control',
                'type' : 'file',
            }
        )
    )
        
    def __init__(self, *args, **kwargs):
        super(ComproForm, self).__init__(*args, **kwargs)
        self.fields['field'].empty_label = 'Please Select'

    error_css_class = 'is-invalid'

    class Meta:
        model = Stakeholder
        
        fields = [
                'name',
                'type',
                'field',
                'address',
                'info',
                'phone',
                'email',
                'kode_pos',
                'landing_page',
                'pic',
            ]

        labels = {
            'name': 'Nama',
            'type': 'Tipe Perusahaan',
            'field': 'Sektor Perusahaan',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'type': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'field': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
            'address': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'info': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'kode_pos': forms.TextInput(
                attrs={
                    'class': 'form-control numberOnly'
                }
            ),
            'landing_page': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'pic': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
        }


class SdmForm(forms.ModelForm):
           
    def __init__(self, *args, **kwargs):
        super(SdmForm, self).__init__(*args, **kwargs)
        self.fields['gender'].empty_label = 'Please Select'

    error_css_class = 'is-invalid'

    class Meta:
        model = Sdm

        exclude = ['stakeholder']
        
        fields = [
                'nama',
                'jabatan',
                'unit_kerja',
                'kompetensi',
                'sertifikat',
                'csirt',
                'narahubung',
                'telepon',
                'gender',
                'email',
            ]

        widgets = {
            'nama': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'jabatan': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'unit_kerja': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'kompetensi': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'sertifikat': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'gender': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
            'csirt': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
            'narahubung': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'telepon': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

class SistemelektronikForm(forms.ModelForm):
           
    def __init__(self, *args, **kwargs):
        super(SistemelektronikForm, self).__init__(*args, **kwargs)

    error_css_class = 'is-invalid'

    class Meta:
        model = Sistemelektronik

        exclude = ['stakeholder']
        
        fields = [
                'nama',
                'spesifikasi',
                'unit',
                'unit_pengelola',
            ]

        widgets = {
            'nama': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'spesifikasi': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'unit': forms.TextInput(
                attrs={
                    'class': 'form-control numberOnly'
                }
            ),
            'unit_pengelola': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

class ProsedurForm(forms.ModelForm):
           
    def __init__(self, *args, **kwargs):
        super(ProsedurForm, self).__init__(*args, **kwargs)

    error_css_class = 'is-invalid'

    class Meta:
        model = Prosedur

        exclude = ['stakeholder']
        
        fields = [
                'nama',
                'nomer',
                'status',
                'tahun',
            ]

        widgets = {
            'nama': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'nomer': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'status': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
            'tahun': forms.TextInput(
                attrs={
                    'class': 'form-control numberOnly'
                }
            ),
        }
        
class ListWorkshopForm(forms.ModelForm):
           
    def __init__(self, *args, **kwargs):
        # get kwargs from view.py
        s_id = kwargs.pop('s_id')

        super(ListWorkshopForm, self).__init__(*args, **kwargs)

        # self.fields['sdm'].empty_label = 'Please Select'
        self.fields['sdm'].queryset = Sdm.objects.filter(stakeholder__id=s_id)
        self.fields['sdm'].required = False

        self.fields['workshop'].empty_label = 'Please Select'

        # sdm = forms.ModelMultipleChoiceField(
        #         label='Nama',
        #         queryset=Sdm.objects.filter(stakeholder__id=s_id), 
        #         widget=forms.CheckboxSelectMultiple(
        #             attrs={
        #                 'class': 'form-control wide'
        #             }
        #         ), 
        #         required=False
        #     )

    error_css_class = 'is-invalid'

    class Meta:
        model = ListWorkshop

        exclude = ['stakeholder']
        
        fields = [
                'sdm',
                'workshop',
                'status',
                'level',
            ]

        widgets = {
            'sdm': forms.CheckboxSelectMultiple(
                attrs={
                    'class': ''
                }
            ),
            'workshop': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
            'level': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
            'status': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
        }