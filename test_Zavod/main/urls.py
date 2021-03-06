from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:id>', views.page),
    path('stat/', views.stat),
    path('<str:name>/', views.tags)
]
