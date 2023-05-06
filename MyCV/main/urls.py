from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('cv', views.cv, name='cv'),
    path('contacts', views.contacts, name='contacts')
]
