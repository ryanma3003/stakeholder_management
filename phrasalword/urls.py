from django.contrib import admin
from django.urls import path

from django.contrib.auth.decorators import login_required

# import views
from .views import (
    PhrasalwordUpdateView,
    showPass,
    )

app_name = 'phrasalword'

urlpatterns = [

    path('update/<slug:pk>', login_required(PhrasalwordUpdateView.as_view()), name='update'),
    path('show_pass', login_required(showPass), name='show_pass'),
]