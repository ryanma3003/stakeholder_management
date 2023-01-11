from django import forms
from .models import *
from django.core.exceptions import ValidationError

class EdukasiForm(forms.ModelForm):
        
    def __init__(self, *args, **kwargs):
        super(EdukasiForm, self).__init__(*args, **kwargs)

    error_css_class = 'is-invalid'

    class Meta:
        model = Edukasi

        exclude = ['stakeholder']
        
        fields = [
                'sosialisasi',
                'tempat',
                'tanggal',
            ]

        labels = {
        }

        widgets = {
            'tempat': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'sosialisasi': forms.Select(
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

            
        }

class PerencanaanForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PerencanaanForm, self).__init__(*args, **kwargs)

    error_css_class = 'is-invalid'

    class Meta:
        model = Perencanaan

        exclude = ['stakeholder']
        
        fields = [
                'draft_sk',
                'no_draft_sk',
                'tgl_draft_sk',
                
                'draft_rfc',
                'no_draft_rfc',
                'tgl_draft_rfc',

                'draft_sumber_daya',
                'no_draft_sumber_daya',
                'tgl_draft_sumber_daya',
            ]

        labels = {
                'draft_sk': 'Draft SK',
                'no_draft_sk': 'Nomor Draft SK',
                'tgl_draft_sk': 'Tanggal Draft SK',
                
                'draft_rfc': 'Draft RFC',
                'no_draft_rfc': 'Nomor Draft RFC',
                'tgl_draft_rfc': 'Tanggal Draft RFC',

                'draft_sumber_daya': 'Draft Sumber Daya',
                'no_draft_sumber_daya': 'Nomor Draft Sumber Daya',
                'tgl_draft_sumber_daya': 'Tanggal Draft Sumber Daya',
            }

        widgets = {
            'draft_sk': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
            'no_draft_sk': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tgl_draft_sk': forms.DateTimeInput(
                attrs={
                    'class': 'datepicker-default form-control',
                    'id': 'datepicker'
                }
            ),

            'draft_rfc': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
            'no_draft_rfc': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tgl_draft_rfc': forms.DateTimeInput(
                attrs={
                    'class': 'datepicker-default form-control',
                    'id': 'datepicker'
                }
            ),

            'draft_sumber_daya': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
            'no_draft_sumber_daya': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tgl_draft_sumber_daya': forms.DateTimeInput(
                attrs={
                    'class': 'datepicker-default form-control',
                    'id': 'datepicker'
                }
            ),

            
        }

class PenerapanForm(forms.ModelForm):

    def clean_file_sk(self):
        file_sk = self.cleaned_data.get('file_sk', False)
        if file_sk:
            if file_sk.name.lower().endswith(('.pdf')) :
                if file_sk.size > 1*1024*1024:
                    raise ValidationError("File too large ( > 1mb )")
                return file_sk
            else :
                raise ValidationError("Not .pdf format")

    def clean_file_rfc(self):
        file_rfc = self.cleaned_data.get('file_rfc', False)
        if file_rfc:
            if file_rfc.name.lower().endswith(('.pdf')) :
                if file_rfc.size > 1*1024*1024:
                    raise ValidationError("File too large ( > 1mb )")
                return file_rfc
            else :
                raise ValidationError("Not .pdf format")

    def clean_file_sumber_daya(self):
        file_sumber_daya = self.cleaned_data.get('file_sumber_daya', False)
        if file_sumber_daya:
            if file_sumber_daya.name.lower().endswith(('.pdf')) :
                if file_sumber_daya.size > 1*1024*1024:
                    raise ValidationError("File too large ( > 1mb )")
                return file_sumber_daya
            else :
                raise ValidationError("Not .pdf format")

    def clean_file_registrasi(self):
        file_registrasi = self.cleaned_data.get('file_registrasi', False)
        if file_registrasi:
            if file_registrasi.name.lower().endswith(('.pdf')) :
                if file_registrasi.size > 1*1024*1024:
                    raise ValidationError("File too large ( > 1mb )")
                return file_registrasi
            else :
                raise ValidationError("Not .pdf format")

    file_sk = forms.FileField(
        label = 'File SK',
        help_text = 'Please use .pdf format and max size 1 megabytes',
        required = False,
        widget = forms.FileInput(
            attrs={
                'class' : 'form-file-input form-control',
                'type' : 'file',
            }
        )
    )

    file_rfc = forms.FileField(
        label = 'File RFC',
        help_text = 'Please use .pdf format and max size 1 megabytes',
        required = False,
        widget = forms.FileInput(
            attrs={
                'class' : 'form-file-input form-control',
                'type' : 'file',
            }
        )
    )

    file_sumber_daya = forms.FileField(
        label = 'File Sumber Daya',
        help_text = 'Please use .pdf format and max size 1 megabytes',
        required = False,
        widget = forms.FileInput(
            attrs={
                'class' : 'form-file-input form-control',
                'type' : 'file',
            }
        )
    )

    file_registrasi = forms.FileField(
        label = 'File Registrasi',
        help_text = 'Please use .pdf format and max size 1 megabytes',
        required = False,
        widget = forms.FileInput(
            attrs={
                'class' : 'form-file-input form-control',
                'type' : 'file',
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super(PenerapanForm, self).__init__(*args, **kwargs)

    error_css_class = 'is-invalid'

    class Meta:
        model = Penerapan

        exclude = ['stakeholder']
        
        fields = [
                'doc_sk',
                'no_doc_sk',
                'tgl_doc_sk',

                'doc_rfc',
                'no_doc_rfc',
                'tgl_doc_rfc',

                'doc_sumber_daya',
                'no_doc_sumber_daya',
                'tgl_doc_sumber_daya',

                'doc_registrasi',
                'no_doc_registrasi',
                'tgl_doc_registrasi',

                'portal_csirt',
                'portal_csirt_url',

                'user'
            ]

        labels = {
                'doc_sk': 'Dokumen SK',
                'no_doc_sk': 'Nomor Dokumen SK',
                'tgl_doc_sk': 'Tanggal Dokumen SK',

                'doc_rfc': 'Dokumen RFC',
                'no_doc_rfc': 'Nomor Dokumen RFC',
                'tgl_doc_rfc': 'Tanggal Dokumen RFC',

                'doc_sumber_daya': 'Dokumen Sumber Daya',
                'no_doc_sumber_daya': 'Nomor Dokumen Sumber Daya',
                'tgl_doc_sumber_daya': 'Tanggal Dokumen Sumber Daya',

                'doc_registrasi' : 'Dokumen Registrasi',
                'no_doc_registrasi' : 'Nomor Dokumen Registrasi',
                'tgl_doc_registrasi' :'Tanggal Pembentukan',

                'portal_csirt': 'Portal TTIS',
                'portal_csirt_url': 'URL Portal TTIS',

                'user': 'PIC',
            }

        widgets = {
            'doc_sk': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
            'no_doc_sk': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tgl_doc_sk': forms.DateTimeInput(
                attrs={
                    'class': 'datepicker-default form-control',
                    'id': 'datepicker'
                }
            ),

            'doc_rfc': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
            'no_doc_rfc': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tgl_doc_rfc': forms.DateTimeInput(
                attrs={
                    'class': 'datepicker-default form-control',
                    'id': 'datepicker'
                }
            ),

            'doc_sumber_daya': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
            'no_doc_sumber_daya': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tgl_doc_sumber_daya': forms.DateTimeInput(
                attrs={
                    'class': 'datepicker-default form-control',
                    'id': 'datepicker'
                }
            ),

            'doc_registrasi': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
            'no_doc_registrasi': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tgl_doc_registrasi': forms.DateTimeInput(
                attrs={
                    'class': 'datepicker-default form-control',
                    'id': 'datepicker'
                }
            ),
            
            'portal_csirt': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
            
            'portal_csirt_url': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            
            'user': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),

            
        }

class PenguatanForm(forms.ModelForm):           
    def __init__(self, *args, **kwargs):
        super(PenguatanForm, self).__init__(*args, **kwargs)

    error_css_class = 'is-invalid'

    class Meta:
        model = Penguatan

        exclude = ['stakeholder']
        
        fields = [
                'status',
            ]

        widgets = {
            'status': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
        }

class EvaluasiForm(forms.ModelForm):  
    def __init__(self, *args, **kwargs):
        super(EvaluasiForm, self).__init__(*args, **kwargs)
        self.fields['tmpi'].empty_label = 'Please Select'

    error_css_class = 'is-invalid'

    class Meta:
        model = Evaluasi

        exclude = ['stakeholder']
        
        fields = [
                'status',
                'tmpi',
            ]

        widgets = {
            'status': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
            'tmpi': forms.Select(
                attrs={
                    'class': 'default-select wide form-control'
                }
            ),
        }
