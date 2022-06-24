from django.urls import path

from django.contrib.auth.decorators import login_required

# import views
from .views import (
    IkamiListView, 
    IkamiDetailView, 
    IkamiCreateView, 
    IkamiUpdateView,
    IkamiDeleteView, 
    )

app_name = 'ikami'

urlpatterns = [

    path('', login_required(IkamiListView.as_view()), name='index'),
    path('create', login_required(IkamiCreateView.as_view()), name='create'),
    path('detail/<slug:pk>', login_required(IkamiDetailView.as_view()), name='detail'),
    path('update/<slug:pk>', login_required(IkamiUpdateView.as_view()), name='update'),
    path('delete/<slug:pk>', login_required(IkamiDeleteView.as_view()), name='delete'),
]