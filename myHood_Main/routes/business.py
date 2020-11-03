from django.urls import path
from myHood_Main.views import business

urlpatterns = [
    path('', business.BusinessListView.as_view(), name='business.index'),
    path('/create', business.BusinessCreateView.as_view(), name='business.create'),
    path('/<int:pk>', business.BusinessDetailView.as_view(), name='business.read'),
    path('/<int:pk>/update', business.BusinessUpdateView.as_view(), name='business.update'),
    path('/<int:pk>/update', business.BusinessDeleteView.as_view(), name='business.delete')
]
