from django.contrib import admin
from django.urls import path
from folio import views


urlpatterns = [
    path('', views.index, name='folio'),
    path('about', views.about, name= 'about'),
    path ('gallery', views.gallery, name='gallery'),
    path('contact', views.contact, name='contact'),
]