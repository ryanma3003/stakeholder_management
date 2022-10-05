from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from django.contrib import messages
from django.http import HttpResponseRedirect, Http404, FileResponse

from .models import *
from .forms import *
from phrasalword.views import decrypt as decrypt_aes
from phrasalword.models import Phrasalword

from PyPDF2 import PdfFileWriter, PdfFileReader
import os

def pdf_view(request, show_id):
    query = Penerapan.objects.get(stakeholder_id = show_id)
    if request.POST.get('file') == 'sk':
        pdf_file = query.file_sk
    elif request.POST.get('file') == 'rfc':
        pdf_file = query.file_rfc
    elif request.POST.get('file') == 'sumber_daya':
        pdf_file = query.file_sumber_daya
    else:
        pdf_file = query.file_registrasi
            
    directory = 'C:\\xampp\\htdocs\\csirt-py\\csirt\\media\\ttis_penerapan'

    out = PdfFileWriter()
    file = PdfFileReader(os.path.join(directory, pdf_file.name.split("/")[-1]))
    password = request.POST.get('passphrase')
    phrasalword = Phrasalword.objects.get(user_id = request.user.id).passphrase
    dec_pass = decrypt_aes(phrasalword)

    if password == dec_pass:
        if file.isEncrypted:
            try:
                file.decrypt(password)
                for idx in range(file.numPages):
                    page = file.getPage(idx)
                    out.addPage(page)
                with open('decrypted_file', 'wb') as f:
                    out.write(f)
                    
                return FileResponse(open('decrypted_file', 'rb'), content_type='application/pdf')
            except FileNotFoundError:
                messages.error(request, "File not found.")
                return HttpResponseRedirect(request.path_info)
    else :
        messages.error(request, "Wrong passphrase.")
        return HttpResponseRedirect(request.path_info)

# Create your views here.
# Edukasi
class EdukasiCreateView(CreateView):
    form_class = EdukasiForm
    template_name = 'ttis/edukasi_create.html'
    extra_context = {
        'title' : 'Edukasi TTIS',
        'breadcrumb': 'Create'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)

        if self.request.GET.__contains__('s_id'):
            kwargs['s_id'] = self.request.GET.get('s_id')

        self.kwargs.update({'s_id' : kwargs['s_id']})
        kwargs = self.kwargs
        return super(EdukasiCreateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        if self.request.GET.__contains__('s_id'):
            self.kwargs['s_id'] = self.request.GET.get('s_id')\

        form.instance.stakeholder_id = self.kwargs['s_id']
        return super().form_valid(form)

class EdukasiUpdateView(UpdateView):
    model = Edukasi
    form_class = EdukasiForm
    template_name = 'ttis/edukasi_create.html'
    extra_context = {
        'title' : 'Edukasi TTIS',
        'breadcrumb': 'Update'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)

        if self.request.GET.__contains__('s_id'):
            kwargs['s_id'] = self.request.GET.get('s_id')

        self.kwargs.update({'s_id' : kwargs['s_id']})
        kwargs = self.kwargs
        return super(EdukasiUpdateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        if self.request.GET.__contains__('s_id'):
            self.kwargs['s_id'] = self.request.GET.get('s_id')

        form.instance.stakeholder_id = self.kwargs['s_id']
        return super().form_valid(form)

class EdukasiDeleteView(DeleteView):
    model = Edukasi

    def get_success_url(self):
        return reverse_lazy('stakeholder:detail', kwargs={'pk': self.object.stakeholder_id})


# Perencanaan
class PerencanaanCreateView(CreateView):
    form_class = PerencanaanForm
    template_name = 'ttis/perencanaan_create.html'
    extra_context = {
        'title' : 'Perencanaan TTIS',
        'breadcrumb': 'Create'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)

        if self.request.GET.__contains__('s_id'):
            kwargs['s_id'] = self.request.GET.get('s_id')

        self.kwargs.update({'s_id' : kwargs['s_id']})
        kwargs = self.kwargs
        return super(PerencanaanCreateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        if self.request.GET.__contains__('s_id'):
            self.kwargs['s_id'] = self.request.GET.get('s_id')

        form.instance.stakeholder_id = self.kwargs['s_id']
        return super().form_valid(form)

class PerencanaanUpdateView(UpdateView):
    model = Perencanaan
    form_class = PerencanaanForm
    template_name = 'ttis/perencanaan_create.html'
    extra_context = {
        'title' : 'Perencanaan TTIS',
        'breadcrumb': 'Update'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)

        if self.request.GET.__contains__('s_id'):
            kwargs['s_id'] = self.request.GET.get('s_id')

        self.kwargs.update({'s_id' : kwargs['s_id']})
        kwargs = self.kwargs
        return super(PerencanaanUpdateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        if self.request.GET.__contains__('s_id'):
            self.kwargs['s_id'] = self.request.GET.get('s_id')

        form.instance.stakeholder_id = self.kwargs['s_id']
        return super().form_valid(form)

class PerencanaanDeleteView(DeleteView):
    model = Perencanaan

    def get_success_url(self):
        return reverse_lazy('stakeholder:detail', kwargs={'pk': self.object.stakeholder_id})

# Penerapan
class PenerapanCreateView(CreateView):
    form_class = PenerapanForm
    template_name = 'ttis/penerapan_create.html'
    extra_context = {
        'title' : 'Penerapan TTIS',
        'breadcrumb': 'Create'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)

        if self.request.GET.__contains__('s_id'):
            kwargs['s_id'] = self.request.GET.get('s_id')

        self.kwargs.update({'s_id' : kwargs['s_id']})
        kwargs = self.kwargs
        return super(PenerapanCreateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        if self.request.GET.__contains__('s_id'):
            self.kwargs['s_id'] = self.request.GET.get('s_id')

        file_sk = self.request.FILES.get('file_sk')
        file_rfc = self.request.FILES.get('file_rfc')
        file_sumber_daya = self.request.FILES.get('file_sumber_daya')
        file_registrasi = self.request.FILES.get('file_registrasi')

        form.instance.stakeholder_id = self.kwargs['s_id']

        penerapan = form.save(commit=False)

        directory = 'C:\\xampp\\htdocs\\csirt-py\\csirt\\media\\ttis_penerapan'
        phrasalword = Phrasalword.objects.get(user_id = self.request.user.id).passphrase
        password = decrypt_aes(phrasalword)

        if file_sk :
            penerapan.file_sk = file_sk
            penerapan.save()
        
            out = PdfFileWriter()
            file_1 = PdfFileReader(os.path.join(directory,file_sk.name))
            
            num = file_1.numPages
            for idx in range(num):
                page = file_1.getPage(idx)
                out.addPage(page)

            out.encrypt(password)
            
            with open(os.path.join(directory,file_sk.name), 'wb') as f:
                out.write(f)

        if file_rfc :
            penerapan.file_rfc = file_rfc
            penerapan.save()
        
            out = PdfFileWriter()
            file_2 = PdfFileReader(os.path.join(directory,file_rfc.name))
            
            num = file_2.numPages
            for idx in range(num):
                page = file_2.getPage(idx)
                out.addPage(page)

            out.encrypt(password)
            
            with open(os.path.join(directory,file_rfc.name), 'wb') as f:
                out.write(f)

        if file_sumber_daya :
            penerapan.file_sumber_daya = file_sumber_daya
            penerapan.save()
        
            out = PdfFileWriter()
            file_3 = PdfFileReader(os.path.join(directory,file_sumber_daya.name))
            
            num = file_3.numPages
            for idx in range(num):
                page = file_3.getPage(idx)
                out.addPage(page)

            out.encrypt(password)
            
            with open(os.path.join(directory,file_sumber_daya.name), 'wb') as f:
                out.write(f)

        if file_registrasi :
            penerapan.file_registrasi = file_registrasi
            penerapan.save()
        
            out = PdfFileWriter()
            file_3 = PdfFileReader(os.path.join(directory,file_registrasi.name))
            
            num = file_3.numPages
            for idx in range(num):
                page = file_3.getPage(idx)
                out.addPage(page)

            out.encrypt(password)
            
            with open(os.path.join(directory,file_registrasi.name), 'wb') as f:
                out.write(f)

        return redirect('stakeholder:detail', self.request.GET.get('s_id'))

class PenerapanUpdateView(UpdateView):
    model = Penerapan
    form_class = PenerapanForm
    template_name = 'ttis/penerapan_create.html'
    extra_context = {
        'title' : 'Penerapan TTIS',
        'breadcrumb': 'Update'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)

        if self.request.GET.__contains__('s_id'):
            kwargs['s_id'] = self.request.GET.get('s_id')

        self.kwargs.update({'s_id' : kwargs['s_id']})
        kwargs = self.kwargs
        return super(PenerapanUpdateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        if self.request.GET.__contains__('s_id'):
            self.kwargs['s_id'] = self.request.GET.get('s_id')

        file_sk = self.request.FILES.get('file_sk')
        file_rfc = self.request.FILES.get('file_rfc')
        file_sumber_daya = self.request.FILES.get('file_sumber_daya')
        file_registrasi = self.request.FILES.get('file_registrasi')

        form.instance.stakeholder_id = self.kwargs['s_id']

        penerapan = form.save(commit=False)

        directory = 'C:\\xampp\\htdocs\\csirt-py\\csirt\\media\\ttis_penerapan'
        phrasalword = Phrasalword.objects.get(user_id = self.request.user.id).passphrase
        password = decrypt_aes(phrasalword)

        if file_sk :
            penerapan.file_sk = file_sk
            penerapan.save()
        
            out = PdfFileWriter()
            file_1 = PdfFileReader(os.path.join(directory,file_sk.name))
            
            num = file_1.numPages
            for idx in range(num):
                page = file_1.getPage(idx)
                out.addPage(page)

            out.encrypt(password)
            
            with open(os.path.join(directory,file_sk.name), 'wb') as f:
                out.write(f)

        if file_rfc :
            penerapan.file_rfc = file_rfc
            penerapan.save()
        
            out = PdfFileWriter()
            file_2 = PdfFileReader(os.path.join(directory,file_rfc.name))
            
            num = file_2.numPages
            for idx in range(num):
                page = file_2.getPage(idx)
                out.addPage(page)

            out.encrypt(password)
            
            with open(os.path.join(directory,file_rfc.name), 'wb') as f:
                out.write(f)

        if file_sumber_daya :
            penerapan.file_sumber_daya = file_sumber_daya
            penerapan.save()
        
            out = PdfFileWriter()
            file_3 = PdfFileReader(os.path.join(directory,file_sumber_daya.name))
            
            num = file_3.numPages
            for idx in range(num):
                page = file_3.getPage(idx)
                out.addPage(page)

            out.encrypt(password)
            
            with open(os.path.join(directory,file_sumber_daya.name), 'wb') as f:
                out.write(f)

        if file_registrasi :
            penerapan.file_registrasi = file_registrasi
            penerapan.save()
        
            out = PdfFileWriter()
            file_3 = PdfFileReader(os.path.join(directory,file_registrasi.name))
            
            num = file_3.numPages
            for idx in range(num):
                page = file_3.getPage(idx)
                out.addPage(page)

            out.encrypt(password)
            
            with open(os.path.join(directory,file_registrasi.name), 'wb') as f:
                out.write(f)

        return redirect('stakeholder:detail', self.request.GET.get('s_id'))

class PenerapanDeleteView(DeleteView):
    model = Penerapan

    def get_success_url(self):
        return reverse_lazy('stakeholder:detail', kwargs={'pk': self.object.stakeholder_id})
    
# Penguatan
class PenguatanCreateView(CreateView):
    form_class = PenguatanForm
    template_name = 'ttis/penguatan_create.html'
    extra_context = {
        'title' : 'Penguatan TTIS',
        'breadcrumb': 'Create'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)

        if self.request.GET.__contains__('s_id'):
            kwargs['s_id'] = self.request.GET.get('s_id')

        self.kwargs.update({'s_id' : kwargs['s_id']})
        kwargs = self.kwargs
        return super(PenguatanCreateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        if self.request.GET.__contains__('s_id'):
            self.kwargs['s_id'] = self.request.GET.get('s_id')

        form.instance.stakeholder_id = self.kwargs['s_id']
        return super().form_valid(form)

class PenguatanUpdateView(UpdateView):
    model = Penguatan
    form_class = PenguatanForm
    template_name = 'ttis/penguatan_create.html'
    extra_context = {
        'title' : 'Penguatan TTIS',
        'breadcrumb': 'Update'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)

        if self.request.GET.__contains__('s_id'):
            kwargs['s_id'] = self.request.GET.get('s_id')

        self.kwargs.update({'s_id' : kwargs['s_id']})
        kwargs = self.kwargs
        return super(PenguatanUpdateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        if self.request.GET.__contains__('s_id'):
            self.kwargs['s_id'] = self.request.GET.get('s_id')

        form.instance.stakeholder_id = self.kwargs['s_id']
        return super().form_valid(form)

class PenguatanDeleteView(DeleteView):
    model = Penguatan

    def get_success_url(self):
        return reverse_lazy('stakeholder:detail', kwargs={'pk': self.object.stakeholder_id})
        
# Evaluasi
class EvaluasiCreateView(CreateView):
    form_class = EvaluasiForm
    template_name = 'ttis/evaluasi_create.html'
    extra_context = {
        'title' : 'Evaluasi TTIS',
        'breadcrumb': 'Create'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)

        if self.request.GET.__contains__('s_id'):
            kwargs['s_id'] = self.request.GET.get('s_id')

        self.kwargs.update({'s_id' : kwargs['s_id']})
        kwargs = self.kwargs
        return super(EvaluasiCreateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        if self.request.GET.__contains__('s_id'):
            self.kwargs['s_id'] = self.request.GET.get('s_id')

        form.instance.stakeholder_id = self.kwargs['s_id']
        return super().form_valid(form)

class EvaluasiUpdateView(UpdateView):
    model = Evaluasi
    form_class = EvaluasiForm
    template_name = 'ttis/evaluasi_create.html'
    extra_context = {
        'title' : 'Evaluasi TTIS',
        'breadcrumb': 'Update'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)

        if self.request.GET.__contains__('s_id'):
            kwargs['s_id'] = self.request.GET.get('s_id')

        self.kwargs.update({'s_id' : kwargs['s_id']})
        kwargs = self.kwargs
        return super(EvaluasiUpdateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        if self.request.GET.__contains__('s_id'):
            self.kwargs['s_id'] = self.request.GET.get('s_id')

        form.instance.stakeholder_id = self.kwargs['s_id']
        return super().form_valid(form)

class EvaluasiDeleteView(DeleteView):
    model = Evaluasi

    def get_success_url(self):
        return reverse_lazy('stakeholder:detail', kwargs={'pk': self.object.stakeholder_id})