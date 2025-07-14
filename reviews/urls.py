from django.urls import path
from . import views
urlpatterns = [
    path('crear/', views.crear_review, name='crear_review'),
    path('', views.ver_reviews, name='ver_reviews'),
]