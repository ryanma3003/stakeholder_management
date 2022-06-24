from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import TemplateView
from django.db.models import Sum, Avg, Count
import json

from compro.models import Stakeholder
from csm.models import Csm
from ikami.models import Ikami
from se.models import Se
# method view

def loginView(request):
    context = {
        'title': 'Sign in to your account'
    }

    user = None

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return render(request, 'auth/login.html', context)

    if request.method == 'POST':
        username_login = request.POST.get('username')
        password_login = request.POST.get('password')

        user = authenticate(request, username=username_login, password=password_login)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')

def logoutView(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    
class DashboardIndexView(TemplateView):
    # inheritance dari TemplateResponseMixin
    # context mixin
    # view
    template_name = 'dashboard/index.html'

    def get_context_data(self, *args, **kwargs):
        
        total_stakeholder = Stakeholder.objects.count()
        total_csm = Csm.objects.count()
        total_se = Se.objects.count()
        total_ikami = Ikami.objects.count()

        # IKAMI
        tata_kelola = Ikami.objects.aggregate(Sum('tata_kelola'))['tata_kelola__sum'] / Ikami.objects.count()
        pengelolaan_risiko = Ikami.objects.aggregate(Sum('pengelolaan_risiko'))['pengelolaan_risiko__sum'] / Ikami.objects.count()
        kerangka_kerja = Ikami.objects.aggregate(Sum('kerangka_kerja'))['kerangka_kerja__sum'] / Ikami.objects.count()
        pengelolaan_aset = Ikami.objects.aggregate(Sum('pengelolaan_aset'))['pengelolaan_aset__sum'] / Ikami.objects.count()
        teknologi_keamanan = Ikami.objects.aggregate(Sum('teknologi_keamanan'))['teknologi_keamanan__sum'] / Ikami.objects.count()
        
        skor_ikami = (tata_kelola + pengelolaan_aset + kerangka_kerja + pengelolaan_risiko + teknologi_keamanan)
        
        if(skor_ikami >= 0 and skor_ikami <= 272):
            evaluasi_ikami = 'Tidak Layak'
        elif(skor_ikami >= 273 and skor_ikami <= 455):
            evaluasi_ikami = 'Pemenuhan Kerangka Kerja Dasar'
        elif(skor_ikami >= 456 and skor_ikami <= 583):
            evaluasi_ikami = 'Cukup Baik'
        elif(skor_ikami >= 584 and skor_ikami <= 645):
            evaluasi_ikami = 'Baik'

        str_tatakelola = "{:}".format(tata_kelola)
        str_pengelolaan_risiko = "{:}".format(pengelolaan_risiko)
        str_kerangka_kerja = "{:}".format(kerangka_kerja)
        str_pengelolaan_aset = "{:}".format(pengelolaan_aset)
        str_teknologi_keamanan = "{:}".format(teknologi_keamanan)

        spider_arr = [str_tatakelola, str_pengelolaan_risiko, str_kerangka_kerja, str_pengelolaan_aset, str_teknologi_keamanan]
        spider_ikami_json = json.dumps(spider_arr)


        # CSM
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

        tatakelola_csm = (avgs['avg_kesadaran'] + avgs['avg_audit'] + avgs['avg_kontrol'] + avgs['avg_pemenuhan'] + avgs['avg_kebijakan'] + avgs['avg_proses']) / 6
        identifikasi = (avgs['avg_manajemen_aset'] + avgs['avg_inventaris'] + avgs['avg_manajemen_risiko'] + avgs['avg_prioritas'] + avgs['avg_pelaporan_identifikasi'] + avgs['avg_klasifikasi']) / 6
        proteksi = (avgs['avg_jaringan'] + avgs['avg_aplikasi'] + avgs['avg_pengguna'] + avgs['avg_manajemen_identitas'] + avgs['avg_cloud'] + avgs['avg_data']) / 6
        deteksi = (avgs['avg_perubahan'] + avgs['avg_monitor'] + avgs['avg_peringatan'] + avgs['avg_pemberitahuan'] + avgs['avg_intelijen'] + avgs['avg_pelaporan_deteksi']) / 6
        respon = (avgs['avg_penahanan'] + avgs['avg_penanggulanan'] + avgs['avg_pemulihan'] + avgs['avg_kegiatan_pasca'] + avgs['avg_pelaporan_respon']) / 5
        maturitas = (tatakelola_csm + identifikasi + proteksi + deteksi + respon) / 5

        str_tatakelola_csm = "{:.2f}".format(tatakelola_csm)
        str_identifikasi = "{:.2f}".format(identifikasi)
        str_proteksi = "{:.2f}".format(proteksi)
        str_deteksi = "{:.2f}".format(deteksi)
        str_respon = "{:.2f}".format(respon)

        spider_csm_arr = [str_tatakelola_csm, str_identifikasi, str_proteksi, str_deteksi, str_respon]
        spider_json = json.dumps(spider_csm_arr)

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

        # Kategorisasi SE
        se_strategis = Se.objects.filter(indeks_ket='strategis').count()
        se_tinggi = Se.objects.filter(indeks_ket='tinggi').count()
        se_rendah = Se.objects.filter(indeks_ket='rendah').count()

        bar_se_arr = [[se_strategis], 
                [se_tinggi],
                [se_rendah],
                ]

        bar_se_json = json.dumps(bar_se_arr)

        context = super(DashboardIndexView, self).get_context_data(**kwargs)
        context['title'] = 'Dashboard'
        context['total_stakeholder'] = total_stakeholder
        context['total_ikami'] = total_ikami
        context['total_csm'] = total_csm
        context['total_se'] = total_se

        context['spider_ikami_json'] = spider_ikami_json
        context['skor_ikami'] = skor_ikami
        context['evaluasi_ikami'] = evaluasi_ikami
        context['ikami1'] = str_tatakelola
        context['ikami2'] = str_pengelolaan_risiko
        context['ikami3'] = str_kerangka_kerja
        context['ikami4'] = str_pengelolaan_aset
        context['ikami5'] = str_teknologi_keamanan

        context['tatakelola'] = tatakelola_csm
        context['identifikasi'] = identifikasi
        context['proteksi'] = proteksi
        context['deteksi'] = deteksi
        context['respon'] = respon
        context['maturitas'] = maturitas
        context['spider_json'] = spider_json
        context['str_tatakelola_csm'] = str_tatakelola_csm
        context['str_identifikasi'] = str_identifikasi
        context['str_proteksi'] = str_proteksi
        context['str_deteksi'] = str_deteksi
        context['str_respon'] = str_respon
        context['bar_json'] = bar_json

        context['bar_se_json'] = bar_se_json

        return context