from django.urls import path

from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('contact/', views.contactView, name='contact'),
    path('success/', views.successView, name='success'),
]