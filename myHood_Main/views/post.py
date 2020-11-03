# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from myHood_Main.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'post/index.html'
    context_object_name = 'posts'


class PostCreateView(CreateView):
    model = Post
    template_name = 'post/create.html'
    fields = ('content', 'author', 'hood',)
    success_url = reverse_lazy('post.index')


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/read.html'
    context_object_name = 'post'


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post/update.html'
    context_object_name = 'post'
    fields = ('content', 'author', 'hood',)

    def get_success_url(self):
        return reverse_lazy('post.read', kwargs={'pk': self.object.id})


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/delete.html'
    success_url = reverse_lazy('post.index')
