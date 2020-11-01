# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from myHood_Main.models import Business


class BusinessListView(ListView):
    model = Business
    template_name = 'business/index.html'
    context_object_name = 'businesses'


class BusinessCreateView(CreateView):
    model = Business
    template_name = 'business/create.html'
    fields = ('name','user','hood','email',)
    success_url = reverse_lazy('business.index')


class BusinessDetailView(DetailView):
    model = Business
    template_name = 'business/read.html'
    context_object_name = 'business'


class BusinessUpdateView(UpdateView):
    model = Business
    template_name = 'business/update.html'
    context_object_name = 'business'
    fields = ('name','user','hood','email',)

    def get_success_url(self):
        return reverse_lazy('business.read', kwargs={'pk': self.object.id})


class BusinessDeleteView(DeleteView):
    model = Business
    template_name = 'business/delete.html'
    success_url = reverse_lazy('business.index')
