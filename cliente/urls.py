from django.urls import path
from . import views

app_name="cliente"

urlpatterns = [
    path("", views.index , name="index" ),
    path("cadastro/", views.cadastro, name="cadastro"),
    path("busca/", views.busca, name="busca"),
    path("busca/<int:cliente>", views.busca, name="buscaum"),
]