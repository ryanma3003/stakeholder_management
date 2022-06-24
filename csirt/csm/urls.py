from django.contrib import admin
from django.urls import path

from django.contrib.auth.decorators import login_required

# import views
from .views import (
    CsmListView, 
    CsmDetailView, 
    CsmCreateView, 
    CsmUpdateView,
    CsmDeleteView, 
    )

app_name = 'csm'

urlpatterns = [

    path('', login_required(CsmListView.as_view()), name='index'),
    path('create', login_required(CsmCreateView.as_view()), name='create'),
    path('detail/<slug:pk>', login_required(CsmDetailView.as_view()), name='detail'),
    path('update/<slug:pk>', login_required(CsmUpdateView.as_view()), name='update'),
    path('delete/<slug:pk>', login_required(CsmDeleteView.as_view()), name='delete'),
]