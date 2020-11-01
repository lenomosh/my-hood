# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from myHood_Main.models import Business


class BusinessListView(ListView):
    model = Business
    template_name = 'location/index.html'
    context_object_name = 'locations'


class BusinessCreateView(CreateView):
    model = Business
    template_name = 'location/create.html'
    fields = ('name',)
    success_url = reverse_lazy('location.index')


class BusinessDetailView(DetailView):
    model = Business
    template_name = 'location/read.html'
    context_object_name = 'location'


class BusinessUpdateView(UpdateView):
    model = Business
    template_name = 'location/update.html'
    context_object_name = 'location'
    fields = ('name',)

    def get_success_url(self):
        return reverse_lazy('location.read', kwargs={'pk': self.object.id})


class BusinessDeleteView(DeleteView):
    model = Business
    template_name = 'location/delete.html'
    success_url = reverse_lazy('location.index')
