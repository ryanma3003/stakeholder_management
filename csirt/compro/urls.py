from django.contrib import admin
from django.urls import path

from django.contrib.auth.decorators import login_required

# import views
from .views import (
    ComproListView, 
    ComproDetailView, 
    ComproCreateView, 
    ComproUpdateView,
    ComproDeleteView,
    SdmCreateView,
    SdmUpdateView,
    SdmDeleteView,
    SistemelektronikCreateView,
    SistemelektronikUpdateView,
    SistemelektronikDeleteView,
    ProsedurCreateView,
    ProsedurUpdateView,
    ProsedurDeleteView,
    ListWorkshopCreateView,
    ListWorkshopUpdateView,
    ListWorkshopDeleteView,
    )

app_name = 'compro'

urlpatterns = [

    path('', login_required(ComproListView.as_view()), name='index'),
    path('create', login_required(ComproCreateView.as_view()), name='create'),
    path('detail/<slug:pk>', login_required(ComproDetailView.as_view()), name='detail'),
    path('update/<slug:pk>', login_required(ComproUpdateView.as_view()), name='update'),
    path('delete/<slug:pk>', login_required(ComproDeleteView.as_view()), name='delete'),
    
    path('sdm/create', login_required(SdmCreateView.as_view()), name='sdm_create'),
    path('sdm/update/<slug:pk>', login_required(SdmUpdateView.as_view()), name='sdm_update'),
    path('sdm/delete/<slug:pk>', login_required(SdmDeleteView.as_view()), name='sdm_delete'),
    
    path('sitemelektronik/create', login_required(SistemelektronikCreateView.as_view()), name='se_create'),
    path('sitemelektronik/update/<slug:pk>', login_required(SistemelektronikUpdateView.as_view()), name='se_update'),
    path('sitemelektronik/delete/<slug:pk>', login_required(SistemelektronikDeleteView.as_view()), name='se_delete'),
    
    path('prosedur/create', login_required(ProsedurCreateView.as_view()), name='pr_create'),
    path('prosedur/update/<slug:pk>', login_required(ProsedurUpdateView.as_view()), name='pr_update'),
    path('prosedur/delete/<slug:pk>', login_required(ProsedurDeleteView.as_view()), name='pr_delete'),
    
    path('listworkshop/create', login_required(ListWorkshopCreateView.as_view()), name='lw_create'),
    path('listworkshop/update/<slug:pk>', login_required(ListWorkshopUpdateView.as_view()), name='lw_update'),
    path('listworkshop/delete/<slug:pk>', login_required(ListWorkshopDeleteView.as_view()), name='lw_delete'),
]