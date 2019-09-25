from django.urls import path,include
from .views import *
from django.conf.urls import url

urlpatterns = [
    path('marca_form',criar_marca, name='criar_marca'),
    path('marca_listar', listar_marca,name='marca_list'),
    path('marca_deletar//(?P<pk>[0-9]+)', deletar_marca, name = 'deletar_marca'),
    path('marca_editar//(?P<pk>[0-9]+',editar_marca,name = 'editar_marca'),
    path('produto_form',criar_produto,name='criar_produto'),
    path('produto_listar',listar_produto,name='listar_produto'),
    path('produto_deletar//(?P<pk>[0-9]+)', deletar_produto,name='deletar_produto'),
    path('produto_editar//(?P<pk>[0-9]+)', editar_produto,name='editar_produto'),
    path('listar_produto_marca//(?P<pk>[0-9]+)',listar_produto_marca,name='listar_produto_marca')
]

