from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.signup_view, name='register'),
    path('perfil/', views.profile_view, name='perfil'),
    path('editar-perfil/', views.edit_profile_view, name='editar_perfil'),
]

