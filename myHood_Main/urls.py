from django.urls import path

from . import views

urlpatterns = [
    path('', views.HoodListView.as_view(), name='hood.index'),
    path('/create', views.HoodCreateView.as_view(), name='hood.create'),
    path('/<int:pk>', views.HoodDetailView.as_view(), name='hood.read'),
    path('/<int:pk>/update', views.HoodUpdateView.as_view(), name='hood.update'),
    path('/<int:pk>/update', views.HoodDeleteView.as_view(), name='hood.delete')
]
