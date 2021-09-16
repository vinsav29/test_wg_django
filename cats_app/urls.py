from django.urls import path
from . import views

urlpatterns = [
    path('ping/', views.ping),
    path('cat/', views.cat),
    path('cats/', views.cats),
]