from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='eventPortal-home'),
    path('about/', views.about, name='eventPortal-about'),
]
