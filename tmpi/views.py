from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
import openpyxl

# Create your views here.

from .models import Tmpi
from .forms import TmpiForm

class SearchList():
    # LoginRequiredMixin
    # login_url = '/login'
    # redirect_field_name = 'redirect_to'

    def get_list_data(self, get_request):
        if len(get_request) == 0:
            search_result = Tmpi.objects.all()
        elif get_request.__contains__('filter'):
            search_result = Tmpi.objects.filter(stakeholder=get_request['filter'])
        else :
            search_result = Tmpi.objects.none()
        return search_result

class TmpiListView(SearchList, ListView):
    model = Tmpi
    context_object_name = 'tmpi_list'
    ordering = ['stakeholder']
    # paginate_by: 3

    def get_queryset(self):
        self.queryset = self.get_list_data(self.request.GET)
        return super(TmpiListView, self).get_queryset()

    def get_context_data(self, *args, **kwargs):
        list_stakeholder = self.model.objects.values('stakeholder', 'stakeholder__name').distinct()
        
        context = super(TmpiListView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Pengukuran TMPI'
        context['list_stakeholder'] = list_stakeholder
        return context

class TmpiDetailView(DetailView):
    model = Tmpi
    extra_context = {}

    def get_context_data(self, *args, **kwargs):

        context = super(TmpiDetailView, self).get_context_data(*args, **kwargs)
        context['title'] = "%s %s" % (self.object.stakeholder, 'Tmpi')
        
        return context

class TmpiCreateView(CreateView):
    form_class = TmpiForm
    template_name = 'tmpi/tmpi_create.html'
    extra_context = {
        'title' : 'Create TMPI',
        'breadcrumb': 'Create'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super(TmpiCreateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        # file_tmpi = form.cleaned_data.get('file_tmpi', False)
        file_tmpi = self.request.FILES.get('file_tmpi')

        if file_tmpi :
            wb = openpyxl.load_workbook(file_tmpi, data_only=True)

            # getting a particular sheet by name out of many sheets
            worksheet = wb["Hasil Perhitungan Tk. Maturitas"]

            # excel_data = list()
            # # iterating over the rows and
            # # getting value from each cell in row
            # for row in worksheet.iter_rows():
            #     row_data = list()
            #     for cell in row:
            #         row_data.append(str(cell.value))
            #     excel_data.append(row_data)

            # form.instance.file_tmpi = file_tmpi
            form.instance.penilaian_kritikalitas = worksheet["Z4"].value if worksheet["Z4"].value else worksheet["AA4"].value
            form.instance.analisis_ancaman = worksheet["Z5"].value if worksheet["Z5"].value else worksheet["AA5"].value
            form.instance.orang_proses_teknologi = worksheet["Z6"].value if worksheet["Z6"].value else worksheet["AA6"].value
            form.instance.lingkungan_kontrol = worksheet["Z7"].value if worksheet["Z7"].value else worksheet["AA7"].value
            form.instance.penilaian_kematangan = worksheet["Z8"].value if worksheet["Z8"].value else worksheet["AA8"].value
            form.instance.total_fase_1 = worksheet["Z9"].value if worksheet["Z9"].value else worksheet["AA9"].value

            form.instance.identifikasi_respon = worksheet["Z10"].value if worksheet["Z10"].value else worksheet["AA10"].value
            form.instance.penyelidikan = worksheet["Z11"].value if worksheet["Z11"].value else worksheet["AA11"].value
            form.instance.aksi = worksheet["Z12"].value if worksheet["Z12"].value else worksheet["AA12"].value
            form.instance.pemulihan = worksheet["Z13"].value if worksheet["Z13"].value else worksheet["AA13"].value
            form.instance.total_fase_2 = worksheet["Z14"].value if worksheet["Z14"].value else worksheet["AA14"].value

            form.instance.identifikasi_tindak_lanjut = worksheet["Z15"].value if worksheet["Z15"].value else worksheet["AA15"].value
            form.instance.pelaporan_review = worksheet["Z16"].value if worksheet["Z16"].value else worksheet["AA16"].value
            form.instance.pembelajaran = worksheet["Z17"].value if worksheet["Z17"].value else worksheet["AA17"].value
            form.instance.pembaruan_informasi = worksheet["Z18"].value if worksheet["Z18"].value else worksheet["AA18"].value
            form.instance.analisis_tren = worksheet["Z19"].value if worksheet["Z19"].value else worksheet["AA19"].value
            form.instance.total_fase_3 = worksheet["Z20"].value if worksheet["Z20"].value else worksheet["AA20"].value

            form.instance.nilai_akhir = worksheet["Z22"].value if worksheet["Z22"].value else worksheet["AA22"].value
        return super().form_valid(form)

class TmpiUpdateView(UpdateView):
    model = Tmpi
    form_class = TmpiForm
    template_name = 'tmpi/tmpi_create.html'
    extra_context = {
        'title' : 'Update TMPI',
        'breadcrumb': 'Update'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super(TmpiUpdateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        file_tmpi = self.request.FILES.get('file_tmpi')

        if file_tmpi :
            wb = openpyxl.load_workbook(file_tmpi, data_only=True)

            # getting a particular sheet by name out of many sheets
            worksheet = wb["Hasil Perhitungan Tk. Maturitas"]

            # form.instance.file_tmpi = file_tmpi
            form.instance.penilaian_kritikalitas = worksheet["Z4"].value if worksheet["Z4"].value else worksheet["AA4"].value
            form.instance.analisis_ancaman = worksheet["Z5"].value if worksheet["Z5"].value else worksheet["AA5"].value
            form.instance.orang_proses_teknologi = worksheet["Z6"].value if worksheet["Z6"].value else worksheet["AA6"].value
            form.instance.lingkungan_kontrol = worksheet["Z7"].value if worksheet["Z7"].value else worksheet["AA7"].value
            form.instance.penilaian_kematangan = worksheet["Z8"].value if worksheet["Z8"].value else worksheet["AA8"].value
            form.instance.total_fase_1 = worksheet["Z9"].value if worksheet["Z9"].value else worksheet["AA9"].value

            form.instance.identifikasi_respon = worksheet["Z10"].value if worksheet["Z10"].value else worksheet["AA10"].value
            form.instance.penyelidikan = worksheet["Z11"].value if worksheet["Z11"].value else worksheet["AA11"].value
            form.instance.aksi = worksheet["Z12"].value if worksheet["Z12"].value else worksheet["AA12"].value
            form.instance.pemulihan = worksheet["Z13"].value if worksheet["Z13"].value else worksheet["AA13"].value
            form.instance.total_fase_2 = worksheet["Z14"].value if worksheet["Z14"].value else worksheet["AA14"].value

            form.instance.identifikasi_tindak_lanjut = worksheet["Z15"].value if worksheet["Z15"].value else worksheet["AA15"].value
            form.instance.pelaporan_review = worksheet["Z16"].value if worksheet["Z16"].value else worksheet["AA16"].value
            form.instance.pembelajaran = worksheet["Z17"].value if worksheet["Z17"].value else worksheet["AA17"].value
            form.instance.pembaruan_informasi = worksheet["Z18"].value if worksheet["Z18"].value else worksheet["AA18"].value
            form.instance.analisis_tren = worksheet["Z19"].value if worksheet["Z19"].value else worksheet["AA19"].value
            form.instance.total_fase_3 = worksheet["Z20"].value if worksheet["Z20"].value else worksheet["AA20"].value

            form.instance.nilai_akhir = worksheet["Z22"].value if worksheet["Z22"].value else worksheet["AA22"].value
        return super().form_valid(form)

class TmpiDeleteView(DeleteView):
    model = Tmpi
    success_url = reverse_lazy('tmpi:index')
