from django.urls import path
from myHood_Main.views import post

urlpatterns = [
    path('', post.PostListView.as_view(), name='post.index'),
    path('/create', post.PostCreateView.as_view(), name='post.create'),
    path('/<int:pk>', post.PostDetailView.as_view(), name='post.read'),
    path('/<int:pk>/update', post.PostUpdateView.as_view(), name='post.update'),
    path('/<int:pk>/update', post.PostDeleteView.as_view(), name='post.delete')
]
