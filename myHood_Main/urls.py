from django.urls import path, include

urlpatterns = [
    path('hood', include('myHood_Main.routes.hood')),
    path('location', include('myHood_Main.routes.location'))
]
