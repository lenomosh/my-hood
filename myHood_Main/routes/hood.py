from django.urls import path
from myHood_Main.views import hood

urlpatterns = [
    path('', hood.HoodListView.as_view(), name='hood.index'),
    path('create', hood.HoodCreateView.as_view(), name='hood.create'),
    path('<int:pk>', hood.HoodDetailView.as_view(), name='hood.read'),
    path('<int:pk>/update', hood.HoodUpdateView.as_view(), name='hood.update'),
    path('<int:pk>/update', hood.HoodDeleteView.as_view(), name='hood.delete')
]
