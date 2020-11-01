# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from myHood_Main.models import Location


class LocationListView(ListView):
    model = Location
    template_name = 'location/index.html'
    context_object_name = 'locations'


class LocationCreateView(CreateView):
    model = Location
    template_name = 'location/create.html'
    fields = ('name',)
    success_url = reverse_lazy('location.index')


class LocationDetailView(DetailView):
    model = Location
    template_name = 'location/read.html'
    context_object_name = 'location'


class LocationUpdateView(UpdateView):
    model = Location
    template_name = 'location/update.html'
    context_object_name = 'location'
    fields = ('name',)

    def get_success_url(self):
        return reverse_lazy('location.read', kwargs={'pk': self.object.id})


class LocationDeleteView(DeleteView):
    model = Location
    template_name = 'location/delete.html'
    success_url = reverse_lazy('location.index')
