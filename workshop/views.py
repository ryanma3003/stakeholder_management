from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
import json

# Create your views here.

from .models import Workshop
from .forms import WorkshopForm

# method view
# Company Profile
class WorkshopListView(ListView):
    model = Workshop
    context_object_name = 'workshop_list'
    ordering = ['id']
    # paginate_by: 3

    def get_context_data(self, *args, **kwargs):
        list_workshop = self.model.objects.values('id', 'nama').distinct()
        
        context = super(WorkshopListView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Peningkatan Kompetensi SDM'
        context['list_workshop'] = list_workshop
        return context

class WorkshopDetailView(DetailView):
    model = Workshop
    extra_context = {}

    def get_context_data(self, *args, **kwargs):

        other_workshop = self.model.objects.exclude(id=self.kwargs.get('pk'))
        # self.extra_context = {'title' : "%s" % (self.object.nama),}
        # self.kwargs.update(self.extra_context)
        # self.kwargs.update({
        #     'other_workshop' : other_workshop,
        #     })

        # kwargs = self.kwargs
        context = super(WorkshopDetailView, self).get_context_data(*args, **kwargs)
        context['title'] = "%s" % (self.object.nama)
        context['other_workshop'] = other_workshop

        return context

class WorkshopCreateView(CreateView):
    form_class = WorkshopForm
    template_name = 'workshop/workshop_create.html'
    extra_context = {
        'title' : 'Create Workshop',
        'breadcrumb': 'Create'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super(WorkshopCreateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        photo = self.request.FILES.get('image')
        if photo :
            form.instance.image = photo
            
        return super().form_valid(form)

class WorkshopUpdateView(UpdateView):
    model = Workshop
    form_class = WorkshopForm
    template_name = 'workshop/workshop_create.html'
    extra_context = {
        'title' : 'Update Workshop',
        'breadcrumb': 'Update'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super(WorkshopUpdateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        photo = self.request.FILES.get('image')
        if photo :
            form.instance.image = photo

        return super().form_valid(form)

class WorkshopDeleteView(DeleteView):
    model = Workshop
    success_url = reverse_lazy('workshop:index')