import { xModal } from "../plugins/xModal/xModal.js";
import { addProduto } from "./addProduto.js";
import { comprarProduto } from "./comprarProduto.js";
import { datatableEstoqueProdutos } from "./datatableEstoqueProdutos.js";
import { detalhesProduto } from "./detalhesProduto.js";
import { venderProduto } from "./venderProduto.js"


$("#compra_produtos").on("click", function(){
    comprarProduto();
});

$("#venda_produtos").on("click", function(){
    venderProduto();
});

$("#novo_produto").on("click", function(){
    addProduto();
});


$("#list_comprados").on("click", function(){
    xModal({
        url: 'modal_produtos_comprados',
        methods: 'POST',
        frame: 'body',
        idModal: '#modalProdutosComprados'
    }).done(function () {
    });
});

$("#list_vendidos").on("click", function(){
    xModal({
        url: 'modal_produtos_vendidos',
        methods: 'POST',
        frame: 'body',
        idModal: '#modalProdutosVendidos'
    }).done(function () {
    });
});

datatableEstoqueProdutos({
    table: "#datatableEstoqueProdutos",
    execute: function() {
        $('#datatableEstoqueProdutos').on('click', 'tbody tr #btnDetalhes', function (e) {
            var data = $(this).parent().parent().parent().parent().DataTable().row($(this).parent().parent()).data();
            detalhesProduto({
                descricao: data[0],
                entrada: data[1],
                saida: data[2],
                saldo: data[3],
                id_produto: data[4],
            });
        });
    }
});