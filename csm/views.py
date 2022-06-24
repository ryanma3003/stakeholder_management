from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.db.models import Sum, Avg
import json

# Create your views here.

from .models import Csm
from .forms import CsmForm

class SearchList():
    # LoginRequiredMixin
    # login_url = '/login'
    # redirect_field_name = 'redirect_to'

    def get_list_data(self, get_request):
        if len(get_request) == 0:
            search_result = Csm.objects.all()
        elif get_request.__contains__('filter'):
            search_result = Csm.objects.filter(stakeholder=get_request['filter'])
        else :
            search_result = Csm.objects.none()
        return search_result

class CsmListView(SearchList, ListView):
    model = Csm
    context_object_name = 'csm_list'
    ordering = ['stakeholder']
    # paginate_by: 3
    extra_context = {
        'title' : 'Stakeholder Csm',
    }

    def get_queryset(self):
        self.queryset = self.get_list_data(self.request.GET)
        return super(CsmListView, self).get_queryset()

    def get_context_data(self, *args, **kwargs):
        list_stakeholder = self.model.objects.values('stakeholder', 'stakeholder__name').distinct()

        
        avgs = Csm.objects.aggregate(
                    avg_kesadaran=Avg('kesadaran'),
                    avg_audit=Avg('audit'),
                    avg_kontrol=Avg('kontrol'),
                    avg_pemenuhan=Avg('pemenuhan'),
                    avg_kebijakan=Avg('kebijakan'),
                    avg_proses=Avg('proses'),
                    avg_manajemen_aset=Avg('manajemen_aset'),
                    avg_inventaris=Avg('inventaris'),
                    avg_manajemen_risiko=Avg('manajemen_risiko'),
                    avg_prioritas=Avg('prioritas'),
                    avg_pelaporan_identifikasi=Avg('pelaporan_identifikasi'),
                    avg_klasifikasi=Avg('klasifikasi'),
                    avg_jaringan=Avg('jaringan'),
                    avg_aplikasi=Avg('aplikasi'),
                    avg_pengguna=Avg('pengguna'),
                    avg_manajemen_identitas=Avg('manajemen_identitas'),
                    avg_cloud=Avg('cloud'),
                    avg_data=Avg('data'),
                    avg_perubahan=Avg('perubahan'),
                    avg_monitor=Avg('monitor'),
                    avg_peringatan=Avg('peringatan'),
                    avg_pemberitahuan=Avg('pemberitahuan'),
                    avg_intelijen=Avg('intelijen'),
                    avg_pelaporan_deteksi=Avg('pelaporan_deteksi'),
                    avg_penahanan=Avg('penahanan'),
                    avg_penanggulanan=Avg('penanggulanan'),
                    avg_pemulihan=Avg('pemulihan'),
                    avg_kegiatan_pasca=Avg('kegiatan_pasca'),
                    avg_pelaporan_respon=Avg('pelaporan_respon')
                )

        tatakelola = (avgs['avg_kesadaran'] + avgs['avg_audit'] + avgs['avg_kontrol'] + avgs['avg_pemenuhan'] + avgs['avg_kebijakan'] + avgs['avg_proses']) / 6
        identifikasi = (avgs['avg_manajemen_aset'] + avgs['avg_inventaris'] + avgs['avg_manajemen_risiko'] + avgs['avg_prioritas'] + avgs['avg_pelaporan_identifikasi'] + avgs['avg_klasifikasi']) / 6
        proteksi = (avgs['avg_jaringan'] + avgs['avg_aplikasi'] + avgs['avg_pengguna'] + avgs['avg_manajemen_identitas'] + avgs['avg_cloud'] + avgs['avg_data']) / 6
        deteksi = (avgs['avg_perubahan'] + avgs['avg_monitor'] + avgs['avg_peringatan'] + avgs['avg_pemberitahuan'] + avgs['avg_intelijen'] + avgs['avg_pelaporan_deteksi']) / 6
        respon = (avgs['avg_penahanan'] + avgs['avg_penanggulanan'] + avgs['avg_pemulihan'] + avgs['avg_kegiatan_pasca'] + avgs['avg_pelaporan_respon']) / 5
        maturitas = (tatakelola + identifikasi + proteksi + deteksi + respon) / 5

        str_tatakelola = "{:.2f}".format(tatakelola)
        str_identifikasi = "{:.2f}".format(identifikasi)
        str_proteksi = "{:.2f}".format(proteksi)
        str_deteksi = "{:.2f}".format(deteksi)
        str_respon = "{:.2f}".format(respon)

        spider_arr = [str_tatakelola, str_identifikasi, str_proteksi, str_deteksi, str_respon]
        spider_json = json.dumps(spider_arr)

        bar_arr = [[float("{:.2f}".format(avgs['avg_kesadaran']))], 
                [float("{:.2f}".format(avgs['avg_audit']))],
                [float("{:.2f}".format(avgs['avg_kontrol']))],
                [float("{:.2f}".format(avgs['avg_pemenuhan']))],
                [float("{:.2f}".format(avgs['avg_kebijakan']))],
                [float("{:.2f}".format(avgs['avg_proses']))],
                [float("{:.2f}".format(avgs['avg_manajemen_aset']))],
                [float("{:.2f}".format(avgs['avg_inventaris']))],
                [float("{:.2f}".format(avgs['avg_manajemen_risiko']))],
                [float("{:.2f}".format(avgs['avg_prioritas']))],
                [float("{:.2f}".format(avgs['avg_pelaporan_identifikasi']))],
                [float("{:.2f}".format(avgs['avg_klasifikasi']))],
                [float("{:.2f}".format(avgs['avg_jaringan']))],
                [float("{:.2f}".format(avgs['avg_aplikasi']))],
                [float("{:.2f}".format(avgs['avg_pengguna']))],
                [float("{:.2f}".format(avgs['avg_manajemen_identitas']))],
                [float("{:.2f}".format(avgs['avg_cloud']))],
                [float("{:.2f}".format(avgs['avg_data']))],
                [float("{:.2f}".format(avgs['avg_perubahan']))],
                [float("{:.2f}".format(avgs['avg_monitor']))],
                [float("{:.2f}".format(avgs['avg_peringatan']))],
                [float("{:.2f}".format(avgs['avg_pemberitahuan']))],
                [float("{:.2f}".format(avgs['avg_intelijen']))],
                [float("{:.2f}".format(avgs['avg_pelaporan_deteksi']))],
                [float("{:.2f}".format(avgs['avg_penahanan']))],
                [float("{:.2f}".format(avgs['avg_penanggulanan']))],
                [float("{:.2f}".format(avgs['avg_pemenuhan']))],
                [float("{:.2f}".format(avgs['avg_kegiatan_pasca']))],
                [float("{:.2f}".format(avgs['avg_pelaporan_respon']))],
                ]

        bar_json = json.dumps(bar_arr)

        other_csm = self.model.objects.exclude(stakeholder=self.kwargs.get('pk'))
        self.kwargs.update({
            'other_csm' : other_csm,
            'tatakelola' : tatakelola,
            'identifikasi' : identifikasi,
            'proteksi' : proteksi,
            'deteksi' : deteksi,
            'respon' : respon,
            'maturitas' : maturitas,
            'spider_json' : spider_json,
            'str_tatakelola' : str_tatakelola,
            'str_identifikasi' : str_identifikasi,
            'str_proteksi' : str_proteksi,
            'str_deteksi' : str_deteksi,
            'str_respon' : str_respon,
            'bar_json' : bar_json,
            'list_stakeholder': list_stakeholder
            })

        kwargs = self.kwargs
        return super(CsmListView, self).get_context_data(*args, **kwargs)

class CsmDetailView(DetailView):
    model = Csm
    extra_context = {}

    def get_context_data(self, *args, **kwargs):
        tatakelola = (self.object.kesadaran + self.object.audit + self.object.kontrol + self.object.pemenuhan + self.object.kebijakan + self.object.proses) / 6
        identifikasi = (self.object.manajemen_aset + self.object.inventaris + self.object.manajemen_risiko + self.object.prioritas + self.object.pelaporan_identifikasi + self.object.klasifikasi) / 6
        proteksi = (self.object.jaringan + self.object.aplikasi + self.object.pengguna + self.object.manajemen_identitas + self.object.cloud + self.object.data) / 6
        deteksi = (self.object.perubahan + self.object.monitor + self.object.peringatan + self.object.pemberitahuan + self.object.intelijen + self.object.pelaporan_deteksi) / 6
        respon = (self.object.penahanan + self.object.penanggulanan + self.object.pemulihan + self.object.kegiatan_pasca + self.object.pelaporan_respon) / 5
        maturitas = (tatakelola + identifikasi + proteksi + deteksi + respon) / 5

        str_tatakelola = "{:.2f}".format(tatakelola)
        str_identifikasi = "{:.2f}".format(identifikasi)
        str_proteksi = "{:.2f}".format(proteksi)
        str_deteksi = "{:.2f}".format(deteksi)
        str_respon = "{:.2f}".format(respon)

        spider_arr = [str_tatakelola, str_identifikasi, str_proteksi, str_deteksi, str_respon]
        spider_json = json.dumps(spider_arr)

        bar_arr = [[float("{:.2f}".format(self.object.kesadaran))], 
                [float("{:.2f}".format(self.object.audit))],
                [float("{:.2f}".format(self.object.kontrol))],
                [float("{:.2f}".format(self.object.pemenuhan))],
                [float("{:.2f}".format(self.object.kebijakan))],
                [float("{:.2f}".format(self.object.proses))],
                [float("{:.2f}".format(self.object.manajemen_aset))],
                [float("{:.2f}".format(self.object.inventaris))],
                [float("{:.2f}".format(self.object.manajemen_risiko))],
                [float("{:.2f}".format(self.object.prioritas))],
                [float("{:.2f}".format(self.object.pelaporan_identifikasi))],
                [float("{:.2f}".format(self.object.klasifikasi))],
                [float("{:.2f}".format(self.object.jaringan))],
                [float("{:.2f}".format(self.object.aplikasi))],
                [float("{:.2f}".format(self.object.pengguna))],
                [float("{:.2f}".format(self.object.manajemen_identitas))],
                [float("{:.2f}".format(self.object.cloud))],
                [float("{:.2f}".format(self.object.data))],
                [float("{:.2f}".format(self.object.perubahan))],
                [float("{:.2f}".format(self.object.monitor))],
                [float("{:.2f}".format(self.object.peringatan))],
                [float("{:.2f}".format(self.object.pemberitahuan))],
                [float("{:.2f}".format(self.object.intelijen))],
                [float("{:.2f}".format(self.object.pelaporan_deteksi))],
                [float("{:.2f}".format(self.object.penahanan))],
                [float("{:.2f}".format(self.object.penanggulanan))],
                [float("{:.2f}".format(self.object.pemenuhan))],
                [float("{:.2f}".format(self.object.kegiatan_pasca))],
                [float("{:.2f}".format(self.object.pelaporan_respon))],
                ]

        bar_json = json.dumps(bar_arr)

        self.extra_context = {'title' : "%s %s" % (self.object.stakeholder, 'CSM'),}
        self.kwargs.update(self.extra_context)

        other_csm = self.model.objects.exclude(stakeholder=self.kwargs.get('pk'))
        self.kwargs.update({
            'other_csm' : other_csm,
            'tatakelola' : tatakelola,
            'identifikasi' : identifikasi,
            'proteksi' : proteksi,
            'deteksi' : deteksi,
            'respon' : respon,
            'maturitas' : maturitas,
            'spider_json' : spider_json,
            'str_tatakelola' : str_tatakelola,
            'str_identifikasi' : str_identifikasi,
            'str_proteksi' : str_proteksi,
            'str_deteksi' : str_deteksi,
            'str_respon' : str_respon,
            'bar_json' : bar_json,
            })

        kwargs = self.kwargs
        return super(CsmDetailView, self).get_context_data(*args, **kwargs)

class CsmCreateView(CreateView):
    form_class = CsmForm
    template_name = 'csm/csm_create.html'
    extra_context = {
        'title' : 'Create Csm',
        'breadcrumb': 'Create'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super(CsmCreateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)

class CsmUpdateView(UpdateView):
    model = Csm
    form_class = CsmForm
    template_name = 'csm/csm_create.html'
    extra_context = {
        'title' : 'Update Csm',
        'breadcrumb': 'Update'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super(CsmUpdateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)

class CsmDeleteView(DeleteView):
    model = Csm
    success_url = reverse_lazy('csm:index')