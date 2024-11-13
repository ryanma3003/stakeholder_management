from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.db.models import Sum
import json

# Create your views here.

from .models import Ikami
from .forms import IkamiForm

class SearchList():
    # LoginRequiredMixin
    # login_url = '/login'
    # redirect_field_name = 'redirect_to'

    def get_list_data(self, get_request):
        if len(get_request) == 0:
            search_result = Ikami.objects.all()
        elif get_request.__contains__('filter'):
            search_result = Ikami.objects.filter(stakeholder=get_request['filter'])
        else :
            search_result = Ikami.objects.none()
        return search_result

# method view
# Company Profile
class IkamiListView(SearchList, ListView):
    model = Ikami
    context_object_name = 'ikami_list'
    ordering = ['stakeholder']
    # paginate_by: 3

    def get_queryset(self):
        self.queryset = self.get_list_data(self.request.GET)
        return super(IkamiListView, self).get_queryset()

    def get_context_data(self, *args, **kwargs):
        list_stakeholder = self.model.objects.values('stakeholder', 'stakeholder__name').distinct()
        
        try:
            tata_kelola = Ikami.objects.aggregate(Sum('tata_kelola'))['tata_kelola__sum'] / Ikami.objects.count()
            pengelolaan_risiko = Ikami.objects.aggregate(Sum('pengelolaan_risiko'))['pengelolaan_risiko__sum'] / Ikami.objects.count()
            kerangka_kerja = Ikami.objects.aggregate(Sum('kerangka_kerja'))['kerangka_kerja__sum'] / Ikami.objects.count()
            pengelolaan_aset = Ikami.objects.aggregate(Sum('pengelolaan_aset'))['pengelolaan_aset__sum'] / Ikami.objects.count()
            teknologi_keamanan = Ikami.objects.aggregate(Sum('teknologi_keamanan'))['teknologi_keamanan__sum'] / Ikami.objects.count()
        
            skor = (tata_kelola + pengelolaan_aset + kerangka_kerja + pengelolaan_risiko + teknologi_keamanan)
        except Ikami.DoesNotExist:
            tata_kelola = 0
            pengelolaan_risiko = 0
            kerangka_kerja = 0
            pengelolaan_aset = 0
            teknologi_keamanan = 0
            skor = 0
        
        if(skor >= 0 and skor <= 272):
            evaluasi = 'Tidak Layak'
        elif(skor >= 273 and skor <= 455):
            evaluasi = 'Pemenuhan Kerangka Kerja Dasar'
        elif(skor >= 456 and skor <= 583):
            evaluasi = 'Cukup Baik'
        elif(skor >= 584 and skor <= 645):
            evaluasi = 'Baik'
        else:
            evaluasi = ''

        str_tatakelola = "{:.2f}".format(tata_kelola)
        str_pengelolaan_risiko = "{:.2f}".format(pengelolaan_risiko)
        str_kerangka_kerja = "{:.2f}".format(kerangka_kerja)
        str_pengelolaan_aset = "{:.2f}".format(pengelolaan_aset)
        str_teknologi_keamanan = "{:.2f}".format(teknologi_keamanan)

        spider_arr = [str_tatakelola, str_pengelolaan_risiko, str_kerangka_kerja, str_pengelolaan_aset, str_teknologi_keamanan]
        spider_json = json.dumps(spider_arr)

        other_ikami = self.model.objects.exclude(stakeholder=self.kwargs.get('pk'))

        context = super(IkamiListView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Stakeholder IKAMI'
        context['list_stakeholder'] = list_stakeholder
        context['other_ikami'] = other_ikami
        context['evaluasi'] = evaluasi
        context['spider_json'] = spider_json
        context['skor'] = skor

        return context

class IkamiDetailView(DetailView):
    model = Ikami
    extra_context = {}

    def get_context_data(self, *args, **kwargs):
        skor = (self.object.tata_kelola + self.object.pengelolaan_aset + self.object.kerangka_kerja + self.object.pengelolaan_risiko + self.object.teknologi_keamanan)
        
        if(skor >= 0 and skor <= 272):
            evaluasi = 'Tidak Layak'
        elif(skor >= 273 and skor <= 455):
            evaluasi = 'Pemenuhan Kerangka Kerja Dasar'
        elif(skor >= 456 and skor <= 583):
            evaluasi = 'Cukup Baik'
        elif(skor >= 584 and skor <= 645):
            evaluasi = 'Baik'
        else:
            evaluasi = ''

        str_tatakelola = "{:}".format(self.object.tata_kelola)
        str_pengelolaan_risiko = "{:}".format(self.object.pengelolaan_risiko)
        str_kerangka_kerja = "{:}".format(self.object.kerangka_kerja)
        str_pengelolaan_aset = "{:}".format(self.object.pengelolaan_aset)
        str_teknologi_keamanan = "{:}".format(self.object.teknologi_keamanan)

        spider_arr = [str_tatakelola, str_pengelolaan_risiko, str_kerangka_kerja, str_pengelolaan_aset, str_teknologi_keamanan]
        spider_json = json.dumps(spider_arr)

        other_ikami = self.model.objects.exclude(stakeholder=self.kwargs.get('pk'))

        context = super(IkamiDetailView, self).get_context_data(*args, **kwargs)
        context['title'] = "%s %s" % (self.object.stakeholder, 'IKAMI')
        context['other_ikami'] = other_ikami
        context['skor'] = skor
        context['evaluasi'] = evaluasi
        context['spider_json'] = spider_json
        context['str_tatakelola'] = str_tatakelola
        context['str_pengelolaan_aset'] = str_pengelolaan_aset
        context['str_kerangka_kerja'] = str_kerangka_kerja
        context['str_pengelolaan_risiko'] = str_pengelolaan_risiko
        context['str_teknologi_keamanan'] = str_teknologi_keamanan
        return context

class IkamiCreateView(CreateView):
    form_class = IkamiForm
    template_name = 'ikami/ikami_create.html'
    extra_context = {
        'title' : 'Create Indeks KAMI',
        'breadcrumb': 'Create'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super(IkamiCreateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)

class IkamiUpdateView(UpdateView):
    model = Ikami
    form_class = IkamiForm
    template_name = 'ikami/ikami_create.html'
    extra_context = {
        'title' : 'Update Indeks KAMI',
        'breadcrumb': 'Update'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super(IkamiUpdateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)

class IkamiDeleteView(DeleteView):
    model = Ikami
    success_url = reverse_lazy('ikami:index')