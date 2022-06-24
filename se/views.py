from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.base import TemplateView, RedirectView, View
from django.views.generic import ListView, DetailView, FormView, CreateView, DeleteView, UpdateView

# auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
from .forms import SeForm
from .models import Se

class SearchList():
    # LoginRequiredMixin
    # login_url = '/login'
    # redirect_field_name = 'redirect_to'

    def get_list_data(self, get_request):
        if len(get_request) == 0:
            search_result = Se.objects.all()
        elif get_request.__contains__('filter'):
            search_result = Se.objects.filter(stakeholder=get_request['filter'])
        else :
            search_result = Se.objects.none()
        return search_result

class SeListView(SearchList, ListView):
    model = Se
    context_object_name = 'se_list'
    ordering = ['stakeholder']
    # paginate_by: 3
    extra_context = {
        'title' : 'Kategorisasi SE',
    }

    def get_queryset(self):
        self.queryset = self.get_list_data(self.request.GET)
        return super(SeListView, self).get_queryset()

    def get_context_data(self, *args, **kwargs):
        list_stakeholder = self.model.objects.values('stakeholder', 'stakeholder__name').distinct()

        self.kwargs.update({'list_stakeholder': list_stakeholder})
        kwargs = self.kwargs
        return super(SeListView, self).get_context_data(*args, **kwargs)

class SeDetailView(DetailView):
    model = Se
    extra_context = {
        'title' : 'Detail SE',
    }

    def get_context_data(self, *args, **kwargs):
        self.kwargs.update(self.extra_context)
        other_se = self.model.objects.exclude(stakeholder=self.kwargs.get('pk'))
        self.kwargs.update({'other_se' : other_se})
        kwargs = self.kwargs
        return super(SeDetailView, self).get_context_data(*args, **kwargs)

class SeFormView(FormView):
    form_class = SeForm
    template_name = 'se/se_create.html'
    success_url = reverse_lazy('se:index')
    extra_context = {
        'title' : 'Create Kategorisasi SE'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super(SeFormView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        if form.cleaned_data.get('indeks_nilai') >= 36 and form.cleaned_data.get('indeks_nilai') <= 50:
            ik = 'Strategis'
        elif form.cleaned_data.get('indeks_nilai') >= 16 and form.cleaned_data.get('indeks_nilai') <= 35:
            ik = 'Tinggi'
        elif form.cleaned_data.get('indeks_nilai') >= 10 and form.cleaned_data.get('indeks_nilai') <= 15:
            ik = 'Rendah'

        form.instance.indeks_ket = ik
        form.save()
        return super(SeFormView, self).form_valid(form)

class SeCreateView(CreateView):
    form_class = SeForm
    template_name = 'se/se_create.html'
    extra_context = {
        'title' : 'Create Kategorisasi SE',
        'breadcrumb': 'Create'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super(SeCreateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        if form.cleaned_data.get('indeks_nilai') >= 36 and form.cleaned_data.get('indeks_nilai') <= 50:
            ik = 'Strategis'
        elif form.cleaned_data.get('indeks_nilai') >= 16 and form.cleaned_data.get('indeks_nilai') <= 35:
            ik = 'Tinggi'
        elif form.cleaned_data.get('indeks_nilai') >= 10 and form.cleaned_data.get('indeks_nilai') <= 15:
            ik = 'Rendah'

        form.instance.indeks_ket = ik
        return super().form_valid(form)

class SeUpdateView(UpdateView):
    model = Se
    form_class = SeForm
    template_name = 'se/se_create.html'
    extra_context = {
        'title' : 'Update Kategorisasi SE',
        'breadcrumb': 'Update'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super(SeUpdateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        if form.cleaned_data.get('indeks_nilai') >= 36 and form.cleaned_data.get('indeks_nilai') <= 50:
            ik = 'Strategis'
        elif form.cleaned_data.get('indeks_nilai') >= 16 and form.cleaned_data.get('indeks_nilai') <= 35:
            ik = 'Tinggi'
        elif form.cleaned_data.get('indeks_nilai') >= 10 and form.cleaned_data.get('indeks_nilai') <= 15:
            ik = 'Rendah'

        form.instance.indeks_ket = ik
        return super().form_valid(form)

class SeDeleteView(DeleteView):
    model = Se
    success_url = reverse_lazy('se:index')


# 
# TEMPLATE VIEW
# 

class SeIndexView(SearchList, TemplateView):
    # inheritance dari TemplateResponseMixin
    # context mixin
    # view
    template_name = 'se/index.html'

    def get_context_data(self, *args, **kwargs):
        # if self.request.GET.__contains__('field_name'):
        #     kwargs['field_name'] = self.request.GET.get('field_name')

        # ses = Se.objects.all()
        ses = self.get_list_data(self.request.GET)
        list_stakeholder = Se.objects.values('stakeholder', 'stakeholder__name').distinct()

        context = super(SeIndexView, self).get_context_data(**kwargs)
        context['title'] = 'Kategorisasi SE'
        context['ses'] = ses
        context['list_stakeholder'] = list_stakeholder
        return context

class SeDelete_View(RedirectView):
    pattern_name = 'se:index'
    permanent = False
    query_string = False

    def get_redirect_url(self, *args, **kwargs):
        delete_id = kwargs.pop('delete_id')
        print(delete_id)
        # Se.objects.get(id=delete_id).delete()
        return super(SeDelete_View, self).get_redirect_url()

class SeForm_View(View):
    template_name = 'se/create.html'
    form = SeForm()
    mode = None
    context = {'title': 'Create Kategorisasi SE', 'breadcrumb': 'Create'}

    def get(self, *args, **kwargs):
        update_id = kwargs.pop('update_id', None)
        if self.mode == 'update':
            se = Se.objects.get(id=update_id)
            data = se.__dict__
            self.form = SeForm(initial=data, instance=se)
            self.context['title'] = 'Update Kategorisasi SE'
            self.context['breadcrumb'] = 'Update'

        self.context = {
            'title' : self.context['title'],
            'breadcrumb' : self.context['breadcrumb'],
            'se_form' : self.form,
        }
        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwargs):
        if kwargs.__contains__('update_id'):
            # update post
            se_update = Se.objects.get(id=kwargs.pop('update_id'))
            self.form = SeForm(self.request.POST, instance=se_update)
        else:
            # create post
            self.form = SeForm(self.request.POST)

        if self.form.is_valid():
            # indeks_ket auto value based on indeks_nilai
            if self.form.cleaned_data.get('indeks_nilai') >= 36 and self.form.cleaned_data.get('indeks_nilai') <= 50:
                ik = 'Strategis'
            elif self.form.cleaned_data.get('indeks_nilai') >= 16 and self.form.cleaned_data.get('indeks_nilai') <= 35:
                ik = 'Tinggi'
            elif self.form.cleaned_data.get('indeks_nilai') >= 10 and self.form.cleaned_data.get('indeks_nilai') <= 15:
                ik = 'Rendah'

            self.form.instance.indeks_ket = ik
            self.form.save()

        return redirect('se:index')

class SePdfView(RedirectView):
    pattern_name = 'se:index'
    # permanent untuk memberitahu server apakah redirect ini sementara atau permanent
    permanent = False
    # query_string untuk menentukan apakah url query digunakan atau tidak
    query_string = False

    def get_redirect_url(self, *args, **kwargs):
        return super(SePdfView, self).get_redirect_url( *args, **kwargs)

# 
# Function Base
# 

def se(request):
    ses = Se.objects.all()

    context = {
        'title' : 'Kategorisasi SE',
        'ses' : ses,
    }
    return render(request, "se/index.html", context)

def se_create(request):
    se_form = SeForm(request.POST or None)
    error = None
    
    if request.method == 'POST':

        if se_form.is_valid():
            if se_form.cleaned_data.get('indeks_nilai') >= 36 and se_form.cleaned_data.get('indeks_nilai') <= 50:
                ik = 'Strategis'
            elif se_form.cleaned_data.get('indeks_nilai') >= 16 and se_form.cleaned_data.get('indeks_nilai') <= 35:
                ik = 'Tinggi'
            elif se_form.cleaned_data.get('indeks_nilai') >= 10 and se_form.cleaned_data.get('indeks_nilai') <= 15:
                ik = 'Rendah'

            # Se.objects.create(
            #     stakeholder = se_form.cleaned_data.get('stakeholder'),
            #     month = se_form.cleaned_data.get('periode'),
            #     year = se_form.cleaned_data.get('year'),
            #     indeks_nilai = se_form.cleaned_data.get('indeks_nilai'),
            #     indeks_ket = ik,
            #     sistem = se_form.cleaned_data.get('sistem'),
            #     keterangan = se_form.cleaned_data.get('keterangan'),
            # )
            se_form.instance.indeks_ket = ik
            se_form.save()

            return redirect("se:index")
        else:
            error = se_form.errors

    context = {
        'title' : 'Kategorisasi SE',
        'se_form' : se_form,
    }

    return render(request, "se/create.html", context)
    
def se_show(request, show_id):
    se = Se.objects.get(id=show_id)

    context = {
        'title' : "%s %s" % (se.stakeholder, 'SE'),
        'se' : se,
    }
    return render(request, "se/show.html", context)

    
def se_edit(request, update_id):
    se = Se.objects.get(id=update_id)

    data = {
        'stakeholder' : se.stakeholder,
        'month' : se.month,
        'year' : se.year,
        'indeks_nilai' : se.indeks_nilai,
        'indeks_ket' : se.indeks_ket,
        'sistem' : se.sistem,
        'keterangan' : se.keterangan,
    }

    se_form = SeForm(request.POST or None, initial=data, instance=se)
    error = None
    
    if request.method == 'POST':

        if se_form.is_valid():
            if se_form.cleaned_data.get('indeks_nilai') >= 36 and se_form.cleaned_data.get('indeks_nilai') <= 50:
                ik = 'Strategis'
            elif se_form.cleaned_data.get('indeks_nilai') >= 16 and se_form.cleaned_data.get('indeks_nilai') <= 35:
                ik = 'Tinggi'
            elif se_form.cleaned_data.get('indeks_nilai') >= 10 and se_form.cleaned_data.get('indeks_nilai') <= 15:
                ik = 'Rendah'
                
            se_form.instance.indeks_ket = ik
            se_form.save()

            return redirect("se:index")
        else:
            error = se_form.errors

    context = {
        'title' : "%s %s" % (se.stakeholder, 'SE'),
        'se' : se,
        'se_form' : se_form
    }
    return render(request, "se/edit.html", context)

def se_delete(request, delete_id):
    se = Se.objects.get(id=delete_id)
    se.delete()

    return redirect("se:index")
