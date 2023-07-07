from django.urls import path
from . import views

urlpatterns = [
    path('<str:url_slug>/', views.index, name="user"),
]