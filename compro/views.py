from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.db.models import Q
import json

# Create your views here.

from .forms import *
from .models import *
from csm.models import Csm
from ikami.models import Ikami
from se.models import Se
from tahap_csirt.models import *

# method view
# Company Profile
class ComproListView(ListView):
    model = Stakeholder
    context_object_name = 'stakeholder_list'
    # for descending order use -
    ordering = ['-id']
    # paginate_by: 3

    def get_context_data(self, *args, **kwargs):
        list_stakeholder = self.model.objects.values('id', 'name').distinct()
        
        context = super(ComproListView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Stakeholder'
        context['list_stakeholder'] = list_stakeholder
        return context

class ComproDetailView(DetailView):
    model = Stakeholder
    # content_type='application/xml'
    extra_context = {}

    def get_context_data(self, *args, **kwargs):

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

        # Tahap CSIRT
        try:
            edu = Edukasi.objects.get(stakeholder_id=self.kwargs.get('pk'))
        except Edukasi.DoesNotExist:
            edu = None

        try:
            edu_sos = Edukasi.objects.get(Q(stakeholder_id=self.kwargs.get('pk')), Q(sosialisasi=1) )
        except Edukasi.DoesNotExist:
            edu_sos = None

        try:
            prn = Perencanaan.objects.get(stakeholder_id=self.kwargs.get('pk'))
        except Perencanaan.DoesNotExist:
            prn = None

        try:
            prn_draft_sk = Perencanaan.objects.get(Q(stakeholder_id=self.kwargs.get('pk')), Q(draft_sk=1) )
        except Perencanaan.DoesNotExist:
            prn_draft_sk = None

        try:
            prn_draft_rfc = Perencanaan.objects.get(Q(stakeholder_id=self.kwargs.get('pk')), Q(draft_rfc=1) )
        except Perencanaan.DoesNotExist:
            prn_draft_rfc = None

        try:
            prn_draft_sd = Perencanaan.objects.get(Q(stakeholder_id=self.kwargs.get('pk')), Q(draft_sumber_daya=1) )
        except Perencanaan.DoesNotExist:
            prn_draft_sd = None

        try:
            pnr = Penerapan.objects.get(stakeholder_id=self.kwargs.get('pk'))
        except Penerapan.DoesNotExist:
            pnr = None

        try:
            pnr_doc_sk = Penerapan.objects.get(Q(stakeholder_id=self.kwargs.get('pk')), Q(doc_sk=1) )
        except Penerapan.DoesNotExist:
            pnr_doc_sk = None

        try:
            pnr_doc_rfc = Penerapan.objects.get(Q(stakeholder_id=self.kwargs.get('pk')), Q(doc_rfc=1) )
        except Penerapan.DoesNotExist:
            pnr_doc_rfc = None

        try:
            pnr_doc_sd = Penerapan.objects.get(Q(stakeholder_id=self.kwargs.get('pk')), Q(doc_sumber_daya=1) )
        except Penerapan.DoesNotExist:
            pnr_doc_sd = None

        try:
            pnr_doc_reg = Penerapan.objects.get(Q(stakeholder_id=self.kwargs.get('pk')), Q(doc_registrasi=1) )
        except Penerapan.DoesNotExist:
            pnr_doc_reg = None

        try:
            pnr_portal = Penerapan.objects.get(Q(stakeholder_id=self.kwargs.get('pk')), Q(portal_csirt=1) )
        except Penerapan.DoesNotExist:
            pnr_portal = None

        try:
            png = Penguatan.objects.get(stakeholder_id=self.kwargs.get('pk'))
        except Penguatan.DoesNotExist:
            png = None

        try:
            png_stat = Penguatan.objects.get(Q(stakeholder_id=self.kwargs.get('pk')), Q(status=1) )
        except Penguatan.DoesNotExist:
            png_stat = None

        try:
            eva = Evaluasi.objects.get(stakeholder_id=self.kwargs.get('pk'))
        except Evaluasi.DoesNotExist:
            eva = None

        try:
            eva_stat = Evaluasi.objects.get(Q(stakeholder_id=self.kwargs.get('pk')), Q(status=1) )
        except Evaluasi.DoesNotExist:
            eva_stat = None

        # Progress
        fulfill = 0
        if edu_sos:
            fulfill += 1
        if prn_draft_sk:
            fulfill += 1
        if prn_draft_rfc:
            fulfill += 1
        if prn_draft_sd:
            fulfill += 1
        if pnr_doc_sk:
            fulfill += 1
        if pnr_doc_rfc:
            fulfill += 1
        if pnr_doc_sd:
            fulfill += 1
        if pnr_doc_reg:
            fulfill += 1
        if pnr_portal:
            fulfill += 1
        if png_stat:
            fulfill += 1
        if eva_stat:
            fulfill += 1

        progress = (fulfill / 11) * 100

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

        # ISO
        try:
            stakeholder_iso = Iso.objects.get(stakeholder_id=self.kwargs.get('pk'))
        except Iso.DoesNotExist:
            stakeholder_iso = None
        
        context = super(ComproDetailView, self).get_context_data(*args, **kwargs)
        context['title'] = "%s %s" % (self.object.name, 'Profile')
        context['narahubung'] = narahubung
        context['csirt'] = csirt
        context['sistemelektronik'] = sistemelektronik
        context['prosedur'] = prosedur
        context['listworkshop'] = listworkshop
        context['stakeholder_iso'] = stakeholder_iso

        context['other_stakeholder'] = other_stakeholder
        context['progress'] = progress
            
        context['tatakelola'] = tatakelola
        context['identifikasi'] = identifikasi
        context['proteksi'] = proteksi
        context['deteksi'] = deteksi
        context['respon'] = respon
        context['maturitas'] = maturitas
        context['spider_json'] = spider_json

        context['skor'] = skor
        context['evaluasi'] = evaluasi
        context['spider_json_ikami'] = spider_json_ikami

        context['indeks_nilai'] = indeks_nilai
        context['indeks_ket'] = indeks_ket

        context['edu'] = edu
        context['prn'] = prn
        context['pnr'] = pnr
        context['png'] = png
        context['eva'] = eva

        return context

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
        photo = self.request.FILES.get('image')
        if photo :
            form.instance.image = photo
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
        photo = self.request.FILES.get('image')
        if photo :
            form.instance.image = photo
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

#Iso
class IsoUpdateView(UpdateView):
    model = Iso
    form_class = IsoForm
    template_name = 'compro/iso_create.html'
    extra_context = {
        'title' : 'Update Stakeholder ISO',
        'breadcrumb': 'Update'
    }

    def get_queryset(self):
        obj, created = self.model.objects.get_or_create(
            stakeholder_id = self.request.GET.get('s_id'),
        )
        return super(IsoUpdateView, self).get_queryset()

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)

        if self.request.GET.__contains__('s_id'):
            kwargs['s_id'] = self.request.GET.get('s_id')

        self.kwargs.update({'s_id' : kwargs['s_id']})
        kwargs = self.kwargs
        return super(IsoUpdateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        if self.request.GET.__contains__('s_id'):
            self.kwargs['s_id'] = self.request.GET.get('s_id')

        form.instance.stakeholder_id = self.kwargs['s_id']
        return super().form_valid(form)