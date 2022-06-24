from django.contrib import admin
from django.urls import path

from django.contrib.auth.decorators import login_required

# import views
from .views import (
    SeListView, 
    SeDetailView, 
    SeFormView, 
    SeCreateView, 
    SeUpdateView,
    SeDeleteView, 
    SeIndexView, 
    SePdfView, 
    SeForm_View, 
    SeDelete_View,
    )

app_name = 'se'

urlpatterns = [

    path('', login_required(SeListView.as_view()), name='index'),
    path('create', login_required(SeCreateView.as_view()), name='create'),
    path('detail/<slug:pk>', login_required(SeDetailView.as_view()), name='detail'),
    path('update/<slug:pk>', login_required(SeUpdateView.as_view()), name='update'),
    path('delete/<slug:pk>', login_required(SeDeleteView.as_view()), name='delete'),

    # path('', SeIndexView.as_view(), name='index'),
    # path('create', SeForm_View.as_view(), name='create'),
    # path('update/<int:update_id>', SeForm_View.as_view(mode='update'), name='update'),
    # path('delete/<int:delete_id>', SeDelete_View.as_view(), name='delete'),
    # path('generate_pdf', SePdfView.as_view(), name='pdf'),
]