from django.urls import path
from .import views

urlpatterns = [
    # Home
    path('', views.index, name="home"),
]