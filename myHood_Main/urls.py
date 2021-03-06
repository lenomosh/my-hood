from django.urls import path, include

urlpatterns = [
    path('hood', include('myHood_Main.routes.hood')),
    path('location', include('myHood_Main.routes.location')),
    path('business', include('myHood_Main.routes.business')),
    path('notification', include('myHood_Main.routes.notification')),
    path('post', include('myHood_Main.routes.post'))
]
