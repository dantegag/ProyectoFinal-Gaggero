from django.urls import path
from . import views
urlpatterns = [
    path('crear/', views.crear_review, name='crear_review'),
    path('', views.ver_reviews, name='ver_reviews'), path('crear/', views.crear_review, name='crear_review'),
    path('ver/', views.ver_reviews, name='ver_reviews'),
    path('editar/<int:pk>/', views.EditarReviewView.as_view(), name='editar_review'),
    path('eliminar/<int:pk>/', views.EliminarReviewView.as_view(), name='eliminar_review'),
]