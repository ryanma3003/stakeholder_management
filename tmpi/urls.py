from django.urls import path

from django.contrib.auth.decorators import login_required

# import views
from .views import (
    TmpiListView, 
    TmpiDetailView, 
    TmpiCreateView, 
    TmpiUpdateView,
    TmpiDeleteView, 
    )

app_name = 'tmpi'

urlpatterns = [

    path('', login_required(TmpiListView.as_view()), name='index'),
    path('create', login_required(TmpiCreateView.as_view()), name='create'),
    path('detail/<slug:pk>', login_required(TmpiDetailView.as_view()), name='detail'),
    path('update/<slug:pk>', login_required(TmpiUpdateView.as_view()), name='update'),
    path('delete/<slug:pk>', login_required(TmpiDeleteView.as_view()), name='delete'),
]