from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from myHood_Main.models import Hood


class HoodListView(ListView):
    model = Hood
    template_name = 'hood/index.html'
    context_object_name = 'hoods'


class HoodCreateView(CreateView):
    model = Hood
    template_name = 'hood/create.html'
    fields = ('name', 'location', 'admin',)
    success_url = reverse_lazy('hood.index')


class HoodDetailView(DetailView):
    model = Hood
    template_name = 'hood/read.html'
    context_object_name = 'hood'


class HoodUpdateView(UpdateView):
    model = Hood
    template_name = 'hood/update.html'
    context_object_name = 'hood'
    fields = ('name', 'location', 'admin',)

    def get_success_url(self):
        return reverse_lazy('hood.read', kwargs={'pk': self.object.id})


class HoodDeleteView(DeleteView):
    model = Hood
    template_name = 'hood/delete.html'
    success_url = reverse_lazy('hood.index')
