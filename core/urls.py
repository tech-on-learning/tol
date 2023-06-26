from django.urls import path
from . import views

urlpatterns = [
    # Errors
    path('400/', views.error_400, name='error400'),
    path('403/', views.error_403, name='error403'),
    path('404/', views.error_404, name='error404'),
    path('500/', views.error_500, name='error500'),
] 