from django.urls import path
from myHood_Main.views import location

urlpatterns = [
    path('', location.LocationListView.as_view(), name='location.index'),
    path('/create', location.LocationCreateView.as_view(), name='location.create'),
    path('/<int:pk>', location.LocationDetailView.as_view(), name='location.read'),
    path('/<int:pk>/update', location.LocationUpdateView.as_view(), name='location.update'),
    path('/<int:pk>/update', location.LocationDeleteView.as_view(), name='location.delete')
]
