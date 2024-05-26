from django.urls import path, include
from .views import IndexView, Quem_SomosView, ContatosView
from .views import grafico

urlpatterns = [
    path('', IndexView.as_view(), name= 'index'),
    path('quem_somos/', Quem_SomosView.as_view(), name= 'quem_somos'),
    path('contatos/', ContatosView.as_view(), name= 'contatos'),
    path('grafico/', grafico, name='grafico'),
]