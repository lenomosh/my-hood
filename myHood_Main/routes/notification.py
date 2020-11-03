from django.urls import path
from myHood_Main.views import notification

urlpatterns = [
    path('', notification.NotificationListView.as_view(), name='notification.index'),
    path('/create', notification.NotificationCreateView.as_view(), name='notification.create'),
    path('/<int:pk>', notification.NotificationDetailView.as_view(), name='notification.read'),
    path('/<int:pk>/update', notification.NotificationUpdateView.as_view(), name='notification.update'),
    path('/<int:pk>/update', notification.NotificationDeleteView.as_view(), name='notification.delete')
]
