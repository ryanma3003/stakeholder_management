from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
import json

# Create your views here.

from .forms import *
from .models import *
from csm.models import Csm
from ikami.models import Ikami
from se.models import Se

# method view
# Company Profile
class ComproListView(ListView):
    model = Stakeholder
    context_object_name = 'stakeholder_list'
    ordering = ['id']
    # paginate_by: 3
    extra_context = {
        'title' : 'Stakeholder',
    }

    def get_context_data(self, *args, **kwargs):
        list_stakeholder = self.model.objects.values('id', 'name').distinct()

        self.kwargs.update({'list_stakeholder': list_stakeholder})
        kwargs = self.kwargs
        return super(ComproListView, self).get_context_data(*args, **kwargs)

class ComproDetailView(DetailView):
    model = Stakeholder
    extra_context = {}

    def get_context_data(self, *args, **kwargs):
        self.extra_context = {'title' : "%s %s" % (self.object.name, 'Profile'),}
        self.kwargs.update(self.extra_context)

        other_stakeholder = self.model.objects.exclude(id=self.kwargs.get('pk'))

        # CSM
        try:
            csm = Csm.objects.get(stakeholder_id=self.kwargs.get('pk'))
            tatakelola = (csm.kesadaran + csm.audit + csm.kontrol + csm.pemenuhan + csm.kebijakan + csm.proses) / 6
            identifikasi = (csm.manajemen_aset + csm.inventaris + csm.manajemen_risiko + csm.prioritas + csm.pelaporan_identifikasi + csm.klasifikasi) / 6
            proteksi = (csm.jaringan + csm.aplikasi + csm.pengguna + csm.manajemen_identitas + csm.cloud + csm.data) / 6
            deteksi = (csm.perubahan + csm.monitor + csm.peringatan + csm.pemberitahuan + csm.intelijen + csm.pelaporan_deteksi) / 6
            respon = (csm.penahanan + csm.penanggulanan + csm.pemulihan + csm.kegiatan_pasca + csm.pelaporan_respon) / 5
            maturitas = (tatakelola + identifikasi + proteksi + deteksi + respon) / 5

            str_tatakelola = "{:.2f}".format(tatakelola)
            str_identifikasi = "{:.2f}".format(identifikasi)
            str_proteksi = "{:.2f}".format(proteksi)
            str_deteksi = "{:.2f}".format(deteksi)
            str_respon = "{:.2f}".format(respon)

            spider_arr = [str_tatakelola, str_identifikasi, str_proteksi, str_deteksi, str_respon]
            spider_json = json.dumps(spider_arr)
        except Csm.DoesNotExist:
            csm = None
            tatakelola = None
            identifikasi = None
            proteksi = None
            deteksi = None
            respon = None
            maturitas = None
            spider_json = None

        # IKAMI
        try:
            ikami = Ikami.objects.get(stakeholder_id=self.kwargs.get('pk'))
            skor = (ikami.tata_kelola + ikami.pengelolaan_aset + ikami.kerangka_kerja + ikami.pengelolaan_risiko + ikami.teknologi_keamanan)
            
            if(skor >= 0 and skor <= 272):
                evaluasi = 'Tidak Layak'
            elif(skor >= 273 and skor <= 455):
                evaluasi = 'Pemenuhan Kerangka Kerja Dasar'
            elif(skor >= 456 and skor <= 583):
                evaluasi = 'Cukup Baik'
            elif(skor >= 584 and skor <= 645):
                evaluasi = 'Baik'

            str_tatakelola_ikami = "{:}".format(ikami.tata_kelola)
            str_pengelolaan_risiko = "{:}".format(ikami.pengelolaan_risiko)
            str_kerangka_kerja = "{:}".format(ikami.kerangka_kerja)
            str_pengelolaan_aset = "{:}".format(ikami.pengelolaan_aset)
            str_teknologi_keamanan = "{:}".format(ikami.teknologi_keamanan)

            spider_arr_ikami = [str_tatakelola_ikami, str_pengelolaan_risiko, str_kerangka_kerja, str_pengelolaan_aset, str_teknologi_keamanan]
            spider_json_ikami = json.dumps(spider_arr_ikami)
        except Ikami.DoesNotExist:
            ikami = None
            skor = None
            evaluasi = None
            str_tatakelola_ikami = None
            str_pengelolaan_risiko = None
            str_kerangka_kerja = None
            str_pengelolaan_aset = None
            str_teknologi_keamanan = None
            spider_json_ikami = None

        # Kategorisasi SE
        try:
            se = Se.objects.get(stakeholder_id=self.kwargs.get('pk'))
            indeks_nilai = se.indeks_nilai
            indeks_ket = se.indeks_ket
        except Se.DoesNotExist:
            se = None
            indeks_nilai = None
            indeks_ket = None

        # Progress
        fulfill = 0
        if csm:
            fulfill += 1
        if ikami:
            fulfill += 1
        if se:
            fulfill += 1

        progress = (fulfill / 3) * 100

        # CSIRT
        try:
            csirt = Sdm.objects.filter(stakeholder_id=self.kwargs.get('pk'), csirt='yes')
        except Sdm.DoesNotExist:
            csirt = None

        # Narahubung
        try:
            narahubung = Sdm.objects.filter(stakeholder_id=self.kwargs.get('pk'), narahubung='yes').first()
        except Sdm.DoesNotExist:
            narahubung = None

        # Sistem Elektronik
        try:
            sistemelektronik = Sistemelektronik.objects.filter(stakeholder_id=self.kwargs.get('pk'))
        except Sistemelektronik.DoesNotExist:
            sistemelektronik = None

        # Prosedur
        try:
            prosedur = Prosedur.objects.filter(stakeholder_id=self.kwargs.get('pk'))
        except Prosedur.DoesNotExist:
            prosedur = None

        # Workshop
        try:
            listworkshop = ListWorkshop.objects.filter(stakeholder_id=self.kwargs.get('pk'))
        except ListWorkshop.DoesNotExist:
            listworkshop = None
        

        self.kwargs.update({
            'narahubung' : narahubung,
            'csirt' : csirt,
            'sistemelektronik' : sistemelektronik,
            'prosedur' : prosedur,
            'listworkshop' : listworkshop,

            'other_stakeholder' : other_stakeholder,
            'progress' : progress,
            
            'tatakelola' : tatakelola,
            'identifikasi' : identifikasi,
            'proteksi' : proteksi,
            'deteksi' : deteksi,
            'respon' : respon,
            'maturitas' : maturitas,
            'spider_json' : spider_json,

            'skor': skor,
            'evaluasi' : evaluasi,
            'spider_json_ikami' : spider_json_ikami,

            'indeks_nilai' : indeks_nilai,
            'indeks_ket' : indeks_ket,
            })

        kwargs = self.kwargs
        return super(ComproDetailView, self).get_context_data(*args, **kwargs)

class ComproCreateView(CreateView):
    form_class = ComproForm
    template_name = 'compro/stakeholder_create.html'
    extra_context = {
        'title' : 'Create Profile',
        'breadcrumb': 'Create'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super(ComproCreateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)

class ComproUpdateView(UpdateView):
    model = Stakeholder
    form_class = ComproForm
    template_name = 'compro/stakeholder_create.html'
    extra_context = {
        'title' : 'Update Stakeholder Profile',
        'breadcrumb': 'Update'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super(ComproUpdateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)

class ComproDeleteView(DeleteView):
    model = Stakeholder
    success_url = reverse_lazy('stakeholder:index')
 

# Sdm
class SdmCreateView(CreateView):
    form_class = SdmForm
    template_name = 'compro/sdm_create.html'
    extra_context = {
        'title' : 'Create Sdm',
        'breadcrumb': 'Create'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)

        if self.request.GET.__contains__('s_id'):
            kwargs['s_id'] = self.request.GET.get('s_id')

        self.kwargs.update({'s_id' : kwargs['s_id']})
        kwargs = self.kwargs
        return super(SdmCreateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        if self.request.GET.__contains__('s_id'):
            self.kwargs['s_id'] = self.request.GET.get('s_id')

        form.instance.stakeholder_id = self.kwargs['s_id']
        return super().form_valid(form)

class SdmUpdateView(UpdateView):
    model = Sdm
    form_class = SdmForm
    template_name = 'compro/sdm_create.html'
    extra_context = {
        'title' : 'Update Stakeholder Sdm',
        'breadcrumb': 'Update'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)

        if self.request.GET.__contains__('s_id'):
            kwargs['s_id'] = self.request.GET.get('s_id')

        self.kwargs.update({'s_id' : kwargs['s_id']})
        kwargs = self.kwargs
        return super(SdmUpdateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        if self.request.GET.__contains__('s_id'):
            self.kwargs['s_id'] = self.request.GET.get('s_id')

        form.instance.stakeholder_id = self.kwargs['s_id']
        return super().form_valid(form)

class SdmDeleteView(DeleteView):
    model = Sdm
    
    # success_url = reverse_lazy('stakeholder:detail')

    def get_success_url(self):
        return reverse_lazy('stakeholder:detail', kwargs={'pk': self.object.stakeholder_id})

    

# Sistem Elektronik
class SistemelektronikCreateView(CreateView):
    form_class = SistemelektronikForm
    template_name = 'compro/sistemelektronik_create.html'
    extra_context = {
        'title' : 'Create Sistem Elektronik',
        'breadcrumb': 'Create'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)

        if self.request.GET.__contains__('s_id'):
            kwargs['s_id'] = self.request.GET.get('s_id')

        self.kwargs.update({'s_id' : kwargs['s_id']})
        kwargs = self.kwargs
        return super(SistemelektronikCreateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        if self.request.GET.__contains__('s_id'):
            self.kwargs['s_id'] = self.request.GET.get('s_id')

        form.instance.stakeholder_id = self.kwargs['s_id']
        return super().form_valid(form)

class SistemelektronikUpdateView(UpdateView):
    model = Sistemelektronik
    form_class = SistemelektronikForm
    template_name = 'compro/sistemelektronik_create.html'
    extra_context = {
        'title' : 'Update Stakeholder Sistem Elektronik',
        'breadcrumb': 'Update'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)

        if self.request.GET.__contains__('s_id'):
            kwargs['s_id'] = self.request.GET.get('s_id')

        self.kwargs.update({'s_id' : kwargs['s_id']})
        kwargs = self.kwargs
        return super(SistemelektronikUpdateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        if self.request.GET.__contains__('s_id'):
            self.kwargs['s_id'] = self.request.GET.get('s_id')

        form.instance.stakeholder_id = self.kwargs['s_id']
        return super().form_valid(form)

class SistemelektronikDeleteView(DeleteView):
    model = Sistemelektronik
    
    # success_url = reverse_lazy('stakeholder:detail')

    def get_success_url(self):
        return reverse_lazy('stakeholder:detail', kwargs={'pk': self.object.stakeholder_id})
    

# Prosedur
class ProsedurCreateView(CreateView):
    form_class = ProsedurForm
    template_name = 'compro/prosedur_create.html'
    extra_context = {
        'title' : 'Create Prosedur',
        'breadcrumb': 'Create'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)

        if self.request.GET.__contains__('s_id'):
            kwargs['s_id'] = self.request.GET.get('s_id')

        self.kwargs.update({'s_id' : kwargs['s_id']})
        kwargs = self.kwargs
        return super(ProsedurCreateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        if self.request.GET.__contains__('s_id'):
            self.kwargs['s_id'] = self.request.GET.get('s_id')

        form.instance.stakeholder_id = self.kwargs['s_id']
        return super().form_valid(form)

class ProsedurUpdateView(UpdateView):
    model = Prosedur
    form_class = ProsedurForm
    template_name = 'compro/prosedur_create.html'
    extra_context = {
        'title' : 'Update Stakeholder Prosedur',
        'breadcrumb': 'Update'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)

        if self.request.GET.__contains__('s_id'):
            kwargs['s_id'] = self.request.GET.get('s_id')

        self.kwargs.update({'s_id' : kwargs['s_id']})
        kwargs = self.kwargs
        return super(ProsedurUpdateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        if self.request.GET.__contains__('s_id'):
            self.kwargs['s_id'] = self.request.GET.get('s_id')

        form.instance.stakeholder_id = self.kwargs['s_id']
        return super().form_valid(form)

class ProsedurDeleteView(DeleteView):
    model = Prosedur
    
    # success_url = reverse_lazy('stakeholder:detail')

    def get_success_url(self):
        return reverse_lazy('stakeholder:detail', kwargs={'pk': self.object.stakeholder_id})


# List Workshop
class ListWorkshopCreateView(CreateView):
    form_class = ListWorkshopForm
    template_name = 'compro/listworkshop_create.html'
    extra_context = {
        'title' : 'Add Workshop',
        'breadcrumb': 'Add'
    }

    # send parameter to form.py
    def get_form_kwargs(self):
        kwargs = super(ListWorkshopCreateView, self).get_form_kwargs()
        s_id = self.request.GET.get('s_id')
        kwargs.update({'s_id': s_id})
        return kwargs

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)

        if self.request.GET.__contains__('s_id'):
            kwargs['s_id'] = self.request.GET.get('s_id')

        self.kwargs.update({'s_id' : kwargs['s_id']})
        kwargs = self.kwargs
        return super(ListWorkshopCreateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        if self.request.GET.__contains__('s_id'):
            self.kwargs['s_id'] = self.request.GET.get('s_id')

        form.instance.stakeholder_id = self.kwargs['s_id']
        return super().form_valid(form)

class ListWorkshopUpdateView(UpdateView):
    model = ListWorkshop
    form_class = ListWorkshopForm
    template_name = 'compro/listworkshop_create.html'
    extra_context = {
        'title' : 'Update Stakeholder Workshop',
        'breadcrumb': 'Update'
    }

    # send parameter to form.py
    def get_form_kwargs(self):
        kwargs = super(ListWorkshopUpdateView, self).get_form_kwargs()
        s_id = self.request.GET.get('s_id')
        kwargs.update({'s_id': s_id})
        return kwargs

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)

        if self.request.GET.__contains__('s_id'):
            kwargs['s_id'] = self.request.GET.get('s_id')

        self.kwargs.update({'s_id' : kwargs['s_id']})
        kwargs = self.kwargs
        return super(ListWorkshopUpdateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        if self.request.GET.__contains__('s_id'):
            self.kwargs['s_id'] = self.request.GET.get('s_id')

        form.instance.stakeholder_id = self.kwargs['s_id']
        return super().form_valid(form)

class ListWorkshopDeleteView(DeleteView):
    model = ListWorkshop

    # success_url = reverse_lazy('stakeholder:detail')

    def get_success_url(self):
        return reverse_lazy('stakeholder:detail', kwargs={'pk': self.object.stakeholder_id})