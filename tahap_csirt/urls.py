from django.urls import path

from django.contrib.auth.decorators import login_required

# import views
from .views import *

app_name = 'tahap_csirt'

urlpatterns = [

    path('edukasi/create', login_required(EdukasiCreateView.as_view()), name='edu_create'),
    path('edukasi/update/<slug:pk>', login_required(EdukasiUpdateView.as_view()), name='edu_update'),
    path('edukasi/delete/<slug:pk>', login_required(EdukasiDeleteView.as_view()), name='edu_delete'),

    path('perencanaan/create', login_required(PerencanaanCreateView.as_view()), name='prn_create'),
    path('perencanaan/update/<slug:pk>', login_required(PerencanaanUpdateView.as_view()), name='prn_update'),
    path('perencanaan/delete/<slug:pk>', login_required(PerencanaanDeleteView.as_view()), name='prn_delete'),

    path('penerapan/create', login_required(PenerapanCreateView.as_view()), name='pnr_create'),
    path('penerapan/update/<slug:pk>', login_required(PenerapanUpdateView.as_view()), name='pnr_update'),
    path('penerapan/show/<int:show_id>', login_required(pdf_view), name='pnr_show'),
    path('penerapan/delete/<slug:pk>', login_required(PenerapanDeleteView.as_view()), name='pnr_delete'),
    
    path('penguatan/create', login_required(PenguatanCreateView.as_view()), name='png_create'),
    path('penguatan/update/<slug:pk>', login_required(PenguatanUpdateView.as_view()), name='png_update'),
    path('penguatan/delete/<slug:pk>', login_required(PenguatanDeleteView.as_view()), name='png_delete'),
    
    path('evaluasi/create', login_required(EvaluasiCreateView.as_view()), name='eva_create'),
    path('evaluasi/update/<slug:pk>', login_required(EvaluasiUpdateView.as_view()), name='eva_update'),
    path('evaluasi/show', login_required(pdf_view), name='eva_show'),
    path('evaluasi/delete/<slug:pk>', login_required(EvaluasiDeleteView.as_view()), name='eva_delete'),
]