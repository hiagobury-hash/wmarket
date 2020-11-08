from django.urls import path
from apps.produtos.views import (
    index,
    modal_compra_produtos,
    salvar_add_produto,
    select_desc_produto,
    salvar_movimentacao_estoque,
    datatable_produtos,
    datatable_estoque_produtos,
    modal_add_produto,
    modal_vender_produtos,
    verificar_estoque,
    verificar_media,
    modal_produtos_comprados,
    modal_produtos_vendidos,
    modal_detalhes_produto,
    datatable_movimentacao_produto
)

urlpatterns = [
    path('', index),
    path('modal_compra_produtos', modal_compra_produtos),
    path('modal_add_produto', modal_add_produto),
    path('modal_vender_produtos', modal_vender_produtos),
    path('salvar_add_produto', salvar_add_produto),
    path('select_desc_produto', select_desc_produto),
    path('salvar_movimentacao_estoque', salvar_movimentacao_estoque),
    path('datatable_produtos', datatable_produtos),
    path('datatable_estoque_produtos', datatable_estoque_produtos),
    path('verificar_estoque', verificar_estoque),
    path('verificar_media', verificar_media),
    path('modal_produtos_comprados', modal_produtos_comprados),
    path('modal_produtos_vendidos', modal_produtos_vendidos),
    path('modal_detalhes_produto', modal_detalhes_produto),
    path('datatable_movimentacao_produto', datatable_movimentacao_produto),
]
