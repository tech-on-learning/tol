from django.urls import path
from .import views

app_name = "courses"

urlpatterns = [
    # Home
    path('', views.index, name="home"),
    path('<slug:course_slug>', views.detail, name="detail"),
]