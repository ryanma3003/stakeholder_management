"""csirt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required

# import views
from .views import loginView, logoutView, DashboardIndexView

urlpatterns = [
    path('', loginView, name='login'),
    path('login/', loginView, name='login'),
    path('admin/', admin.site.urls),

    path('dashboard/', login_required(DashboardIndexView.as_view()), name='home'),

    path('stakeholder/', include('compro.urls', namespace='stakeholder')),
    path('csm/', include('csm.urls', namespace='csm')),
    path('se/', include('se.urls', namespace='se')),
    path('ikami/', include('ikami.urls', namespace='ikami')),
    path('kompetensi/', include('workshop.urls', namespace='workshop')),

    path('logout/', login_required(logoutView), name='logout'),
]
