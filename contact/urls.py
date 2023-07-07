from django.urls import path
from .import views

app_name = "contact"

urlpatterns = [
    # Home
    path('', views.index, name="home"),
    path('become-student/', views.student, name="student"),
    path('become-teacher/', views.teacher, name="teacher"),
]