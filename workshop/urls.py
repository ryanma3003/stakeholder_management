from django.urls import path

from django.contrib.auth.decorators import login_required

# import views
from .views import (
    WorkshopListView, 
    WorkshopDetailView, 
    WorkshopCreateView, 
    WorkshopUpdateView,
    WorkshopDeleteView, 
    )

app_name = 'workshop'

urlpatterns = [

    path('', login_required(WorkshopListView.as_view()), name='index'),
    path('create', login_required(WorkshopCreateView.as_view()), name='create'),
    path('detail/<slug:pk>', login_required(WorkshopDetailView.as_view()), name='detail'),
    path('update/<slug:pk>', login_required(WorkshopUpdateView.as_view()), name='update'),
    path('delete/<slug:pk>', login_required(WorkshopDeleteView.as_view()), name='delete'),
]