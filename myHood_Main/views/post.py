# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from myHood_Main.models import Post, Hood


class PostListView(ListView):
    model = Post
    template_name = 'post/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        new_context = Post.objects.filter(
            hood_id=self.request.user.hood_name.id,
        ).order_by('CREATED_AT')
        return new_context


class PostCreateView(CreateView):

    model = Post
    template_name = 'post/create.html'
    fields = ('content',)
    success_url = reverse_lazy('post.index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.hood = Hood.objects.get(pk=self.request.user.hood_name.id)
        return super(PostCreateView, self).form_valid(form)


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
