# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from myHood_Main.models import Notification


class NotificationListView(ListView):
    model = Notification
    template_name = 'notification/index.html'
    context_object_name = 'notifications'

    def get_queryset(self):
        new_context = Notification.objects.filter(
            hood_id=self.request.user.hood_name.id,
        )
        return new_context


class NotificationCreateView(CreateView):
    model = Notification
    template_name = 'notification/create.html'
    fields = ('name', 'user', 'email')
    success_url = reverse_lazy('notification.index')

    def form_valid(self, form):
        form.instance.hood = self.request.user.hood_name
        return super(NotificationCreateView, self).form_valid(form)


class NotificationDetailView(DetailView):
    model = Notification
    template_name = 'notification/read.html'
    context_object_name = 'notification'


class NotificationUpdateView(UpdateView):
    model = Notification
    template_name = 'notification/update.html'
    context_object_name = 'notification'
    fields = ('name', 'user', 'hood', 'email',)

    def get_success_url(self):
        return reverse_lazy('notification.read', kwargs={'pk': self.object.id})


class NotificationDeleteView(DeleteView):
    model = Notification
    template_name = 'notification/delete.html'
    success_url = reverse_lazy('notification.index')
