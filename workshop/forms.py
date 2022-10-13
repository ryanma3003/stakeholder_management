from django import forms
from .models import Workshop
from django.core.exceptions import ValidationError

class WorkshopForm(forms.ModelForm):

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.name.lower().endswith(('.png', '.jpg', '.jpeg')) :
                if image.size > 1*1024*1024:
                    raise ValidationError("Image file too large ( > 1mn )")
                return image
            else :
                raise ValidationError("File is not an image.")

    image = forms.FileField(
        label = 'Image',
        required = False,
        help_text = 'Please use format .png, .jpg, or .jpeg and max 1 megabytes',
        widget = forms.FileInput(
            attrs={
                'class' : 'form-file-input form-control',
                'type' : 'file',
            }
        )
    )
        
    def __init__(self, *args, **kwargs):
        super(WorkshopForm, self).__init__(*args, **kwargs)

    error_css_class = 'is-invalid'

    class Meta:
        model = Workshop
        
        fields = [
                'nama',
                'jenis',
                'tanggal',
                'lokasi',
                'deskripsi',
            ]

        labels = {
            'jenis': 'Jenis Kegiatan',
        }

        widgets = {
            'nama': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'jenis': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
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
            'deskripsi': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }