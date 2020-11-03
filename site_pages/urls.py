from django.urls import path
from site_pages import views
urlpatterns =[
    path("", views.index,name='pages.index')
]