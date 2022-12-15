from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.db.models import Sum, Avg, Count
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from notifications.signals import notify
from notifications.models import Notification
import json

from compro.models import Stakeholder
from csm.models import Csm
from ikami.models import Ikami
from se.models import Se
from workshop.models import Workshop
from tahap_csirt.models import *

from django.views.decorators.http import require_http_methods

# method view
def handler404(request, exception):
    context = {'foo': 'bar'}
    return render(request, 'error/404.html', context) 

def handler500(request, exception=None):
    context = {'foo': 'bar'}
    return render(request, 'error/500.html', context) 

def showPassChat(request):
    check = request.user.check_password(request.POST['password'])
    Notification.objects.mark_all_as_read()

    if request.method == 'POST' and check:
        return HttpResponse(json.dumps({'success': check}), content_type="application/json")

    return HttpResponse(json.dumps({}), content_type="application/json")

def messageView(request):
    try:
        if request.method == 'POST':
            sender = get_user_model().objects.get(username=request.user)
            receiver = get_user_model().objects.get(id=request.POST.get('user_id'))
            notify.send(sender, recipient=receiver, verb='Message', description=request.POST.get('message'))
            return redirect('stakeholder:detail', request.GET.get('s_id'))
        else:
            return HttpResponse("Invalid request")
    except Exception as e:
        print(e)
        return HttpResponse("Please login from admin site for sending messages")

def messageReplyView(request):
    try:
        if request.method == 'POST':
            sender = get_user_model().objects.get(username=request.user)
            receiver = get_user_model().objects.get(id=request.POST.get('user_id'))
            Notification.objects.mark_all_as_read()
            notify.send(sender, recipient=receiver, verb='Message', level='warning', description=request.POST.get('message'))
            return redirect('home')
        else:
            return HttpResponse("Invalid request")
    except Exception as e:
        print(e)
        return HttpResponse("Please login from admin site for sending messages")

@require_http_methods(["GET", "POST"])
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

class LandingPageView(TemplateView):
    template_name = 'landing/index.html'

    def get_context_data(self, *args, **kwargs):

        kegiatans = Workshop.objects.order_by('-id')[:10]
        context = super(LandingPageView, self).get_context_data(**kwargs)
        context['kegiatans'] = kegiatans
        return context

class KegiatanShowView(DetailView):
    query_pk_and_slug = 'slug'
    template_name = 'landing/berita.html'
    context_object_name = 'post'
    model = Workshop

    def get_context_data(self, *args, **kwargs):

        context = super(KegiatanShowView, self).get_context_data(**kwargs)
        return context

class UserView(TemplateView):
    template_name = 'user/index.html'

    def get_context_data(self, *args, **kwargs):
        
        User = get_user_model()
        users = User.objects.all()
        context = super(UserView, self).get_context_data(**kwargs)
        context['title'] = 'User List'
        context['list_user'] = users
        return context
    
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
        total_workshop = Workshop.objects.count()

        total_edukasi = Edukasi.objects.count()
        total_perencanaan = Perencanaan.objects.count()
        total_penerapan = Penerapan.objects.count()
        total_penguatan = Penguatan.objects.count()
        total_evaluasi = Evaluasi.objects.count()

        # TTIS
        overall_edukasi = "{:.2f}".format((total_edukasi / total_stakeholder) * 100) if total_stakeholder > 0 else 0
        overall_perencanaan = "{:.2f}".format((total_perencanaan / total_stakeholder) * 100) if total_stakeholder > 0 else 0
        overall_penerapan = "{:.2f}".format((total_penerapan / total_stakeholder) * 100) if total_stakeholder > 0 else 0
        overall_penguatan = "{:.2f}".format((total_penguatan / total_stakeholder) * 100) if total_stakeholder > 0 else 0
        overall_evaluasi = "{:.2f}".format((total_evaluasi / total_stakeholder) * 100) if total_stakeholder > 0 else 0

        # IKAMI
        tata_kelola = Ikami.objects.aggregate(Sum('tata_kelola'))['tata_kelola__sum'] / Ikami.objects.count() if total_ikami > 0 else 0
        pengelolaan_risiko = Ikami.objects.aggregate(Sum('pengelolaan_risiko'))['pengelolaan_risiko__sum'] / Ikami.objects.count() if total_ikami > 0 else 0
        kerangka_kerja = Ikami.objects.aggregate(Sum('kerangka_kerja'))['kerangka_kerja__sum'] / Ikami.objects.count() if total_ikami > 0 else 0
        pengelolaan_aset = Ikami.objects.aggregate(Sum('pengelolaan_aset'))['pengelolaan_aset__sum'] / Ikami.objects.count() if total_ikami > 0 else 0
        teknologi_keamanan = Ikami.objects.aggregate(Sum('teknologi_keamanan'))['teknologi_keamanan__sum'] / Ikami.objects.count() if total_ikami > 0 else 0
        
        skor_ikami = (tata_kelola + pengelolaan_aset + kerangka_kerja + pengelolaan_risiko + teknologi_keamanan)
        
        if(skor_ikami >= 0 and skor_ikami <= 272):
            evaluasi_ikami = 'Tidak Layak'
        elif(skor_ikami >= 273 and skor_ikami <= 455):
            evaluasi_ikami = 'Pemenuhan Kerangka Kerja Dasar'
        elif(skor_ikami >= 456 and skor_ikami <= 583):
            evaluasi_ikami = 'Cukup Baik'
        elif(skor_ikami >= 584 and skor_ikami <= 645):
            evaluasi_ikami = 'Baik'

        str_tatakelola = "{:.2f}".format(tata_kelola)
        str_pengelolaan_risiko = "{:.2f}".format(pengelolaan_risiko)
        str_kerangka_kerja = "{:.2f}".format(kerangka_kerja)
        str_pengelolaan_aset = "{:.2f}".format(pengelolaan_aset)
        str_teknologi_keamanan = "{:.2f}".format(teknologi_keamanan)

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

        tatakelola_csm = (avgs['avg_kesadaran'] + avgs['avg_audit'] + avgs['avg_kontrol'] + avgs['avg_pemenuhan'] + avgs['avg_kebijakan'] + avgs['avg_proses']) / 6 if total_csm > 0 else 0
        identifikasi = (avgs['avg_manajemen_aset'] + avgs['avg_inventaris'] + avgs['avg_manajemen_risiko'] + avgs['avg_prioritas'] + avgs['avg_pelaporan_identifikasi'] + avgs['avg_klasifikasi']) / 6 if total_csm > 0 else 0
        proteksi = (avgs['avg_jaringan'] + avgs['avg_aplikasi'] + avgs['avg_pengguna'] + avgs['avg_manajemen_identitas'] + avgs['avg_cloud'] + avgs['avg_data']) / 6 if total_csm > 0 else 0
        deteksi = (avgs['avg_perubahan'] + avgs['avg_monitor'] + avgs['avg_peringatan'] + avgs['avg_pemberitahuan'] + avgs['avg_intelijen'] + avgs['avg_pelaporan_deteksi']) / 6 if total_csm > 0 else 0
        respon = (avgs['avg_penahanan'] + avgs['avg_penanggulanan'] + avgs['avg_pemulihan'] + avgs['avg_kegiatan_pasca'] + avgs['avg_pelaporan_respon']) / 5 if total_csm > 0 else 0
        maturitas = (tatakelola_csm + identifikasi + proteksi + deteksi + respon) / 5 if total_csm > 0 else 0

        str_tatakelola_csm = "{:.2f}".format(tatakelola_csm)
        str_identifikasi = "{:.2f}".format(identifikasi)
        str_proteksi = "{:.2f}".format(proteksi)
        str_deteksi = "{:.2f}".format(deteksi)
        str_respon = "{:.2f}".format(respon)

        spider_csm_arr = [str_tatakelola_csm, str_identifikasi, str_proteksi, str_deteksi, str_respon]
        spider_json = json.dumps(spider_csm_arr)

        bar_arr = [[float("{:.2f}".format(avgs['avg_kesadaran'])) if total_csm > 0 else 0], 
                [float("{:.2f}".format(avgs['avg_audit'])) if total_csm > 0 else 0],
                [float("{:.2f}".format(avgs['avg_kontrol'])) if total_csm > 0 else 0],
                [float("{:.2f}".format(avgs['avg_pemenuhan'])) if total_csm > 0 else 0],
                [float("{:.2f}".format(avgs['avg_kebijakan'])) if total_csm > 0 else 0],
                [float("{:.2f}".format(avgs['avg_proses'])) if total_csm > 0 else 0],
                [float("{:.2f}".format(avgs['avg_manajemen_aset'])) if total_csm > 0 else 0],
                [float("{:.2f}".format(avgs['avg_inventaris'])) if total_csm > 0 else 0],
                [float("{:.2f}".format(avgs['avg_manajemen_risiko'])) if total_csm > 0 else 0],
                [float("{:.2f}".format(avgs['avg_prioritas'])) if total_csm > 0 else 0],
                [float("{:.2f}".format(avgs['avg_pelaporan_identifikasi'])) if total_csm > 0 else 0],
                [float("{:.2f}".format(avgs['avg_klasifikasi'])) if total_csm > 0 else 0],
                [float("{:.2f}".format(avgs['avg_jaringan'])) if total_csm > 0 else 0],
                [float("{:.2f}".format(avgs['avg_aplikasi'])) if total_csm > 0 else 0],
                [float("{:.2f}".format(avgs['avg_pengguna'])) if total_csm > 0 else 0],
                [float("{:.2f}".format(avgs['avg_manajemen_identitas'])) if total_csm > 0 else 0],
                [float("{:.2f}".format(avgs['avg_cloud'])) if total_csm > 0 else 0],
                [float("{:.2f}".format(avgs['avg_data'])) if total_csm > 0 else 0],
                [float("{:.2f}".format(avgs['avg_perubahan'])) if total_csm > 0 else 0],
                [float("{:.2f}".format(avgs['avg_monitor'])) if total_csm > 0 else 0],
                [float("{:.2f}".format(avgs['avg_peringatan'])) if total_csm > 0 else 0],
                [float("{:.2f}".format(avgs['avg_pemberitahuan'])) if total_csm > 0 else 0],
                [float("{:.2f}".format(avgs['avg_intelijen'])) if total_csm > 0 else 0],
                [float("{:.2f}".format(avgs['avg_pelaporan_deteksi'])) if total_csm > 0 else 0],
                [float("{:.2f}".format(avgs['avg_penahanan'])) if total_csm > 0 else 0],
                [float("{:.2f}".format(avgs['avg_penanggulanan'])) if total_csm > 0 else 0],
                [float("{:.2f}".format(avgs['avg_pemenuhan'])) if total_csm > 0 else 0],
                [float("{:.2f}".format(avgs['avg_kegiatan_pasca'])) if total_csm > 0 else 0],
                [float("{:.2f}".format(avgs['avg_pelaporan_respon'])) if total_csm > 0 else 0],
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

        pie_ttis_arr = [[overall_edukasi], 
                [overall_perencanaan],
                [overall_penerapan],
                [overall_penguatan],
                [overall_evaluasi],
                ]

        pie_ttis_json = json.dumps(pie_ttis_arr)

        context = super(DashboardIndexView, self).get_context_data(**kwargs)
        context['title'] = 'Dashboard'
        context['total_stakeholder'] = total_stakeholder
        context['total_ikami'] = total_ikami
        context['total_csm'] = total_csm
        context['total_se'] = total_se
        context['total_workshop'] = total_workshop

        context['total_edukasi'] = total_edukasi
        context['total_perencanaan'] = total_perencanaan
        context['total_penerapan'] = total_penerapan
        context['total_penguatan'] = total_penguatan
        context['total_evaluasi'] = total_evaluasi

        context['overall_edukasi'] = overall_edukasi
        context['overall_perencanaan'] = overall_perencanaan
        context['overall_penerapan'] = overall_penerapan
        context['overall_penguatan'] = overall_penguatan
        context['overall_evaluasi'] = overall_evaluasi
        context['pie_ttis_json'] = pie_ttis_json

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