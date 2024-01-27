from django.urls import path
from . import views


urlpatterns = [
    path('cadastro/', views.cadastro),
    path('login/', views.login),
    path('', views.auth)
]