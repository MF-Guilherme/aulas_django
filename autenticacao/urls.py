from django.urls import path
from . import views


urlpatterns = [
    path('cadastro/', views.cadastro),
    path('valida_formulario/', views.valida_formulario, name='valida_formulario'),
]