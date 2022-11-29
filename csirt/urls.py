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
from django.conf.urls.static import static
from django.conf import settings
import notifications.urls
from django.urls import re_path as url

# import views
from .views import showPassChat, messageView, messageReplyView, loginView, logoutView, DashboardIndexView, UserView, LandingPageView, KegiatanShowView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
    path('kegiatan/<slug:slug>', KegiatanShowView.as_view(), name='kegiatan'),
    path('login/', loginView, name='login'),
    path('admin/', admin.site.urls),

    path('dashboard/', login_required(DashboardIndexView.as_view()), name='home'),
    path('user/', login_required(UserView.as_view()), name='user'),

    path('stakeholder/', include('compro.urls', namespace='stakeholder')),
    path('csm/', include('csm.urls', namespace='csm')),
    path('se/', include('se.urls', namespace='se')),
    path('ikami/', include('ikami.urls', namespace='ikami')),
    path('tmpi/', include('tmpi.urls', namespace='tmpi')),
    path('kompetensi/', include('workshop.urls', namespace='workshop')),
    path('ttis/', include('tahap_csirt.urls', namespace='ttis')),
    path('profile/', include('phrasalword.urls', namespace='profile')),

    path('message', login_required(messageView), name='message'),
    path('messageReply', login_required(messageReplyView), name='messageReply'),
    path('showPassChat', login_required(showPassChat), name='showPassChat'),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),

    path('logout/', login_required(logoutView), name='logout'),
]

handler404 = 'csirt.views.handler404'
handler500 = 'csirt.views.handler500'

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
