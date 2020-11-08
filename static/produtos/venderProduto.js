import { xModal } from "../plugins/xModal/xModal.js";
import { selectDescProduto } from "./selectDescProduto.js";
import { salvarMovimentacaoEstoque } from "./salvarMovimentacaoEstoque.js"
import { verificarEstoque } from "./verificarEstoque.js";
import { verificarMedia } from "./verificarMedia.js";


export function venderProduto(params) {
    xModal({
        url: 'modal_vender_produtos',
        methods: 'POST',
        frame: 'body',
        idModal: '#modalVenderProdutos'
    }).done(function () {

        selectDescProduto({
            input: "#venderDescProduto",
            execute: function() {
                verificarEstoque({
                    id_produto: $("#venderDescProduto").data().id
                }).done(function(data){
                    $("#saldoVenda").text("Saldo: " + data.saldo);
                });

                verificarMedia({
                    id_produto: $("#venderDescProduto").data().id,
                    tipo: "S"
                }).done(function(data){
                    $("#mediaVenda").text("Média de Venda: " + data.media);
                });

                verificarMedia({
                    id_produto: $("#venderDescProduto").data().id,
                    tipo: "E"
                }).done(function(data){
                    $("#vdMediaCompra").text("Média de Compra: " + data.media);
                });
            }
        });

        $("#salvarMovimentacaoEstoqueVenda").on("click", function () {
            salvarMovimentacaoEstoque({
                id_produto: $("#venderDescProduto").data().id,
                quantidade:  $("#venderQtdProduto").val(),
                valor:  $("#venderVlVenda").val(),
                tipo: 'S',
                execute: function(){
                    verificarEstoque({
                        id_produto: $("#venderDescProduto").data().id
                    }).done(function(data){
                        $("#saldoVenda").text("Saldo: " + data.saldo);
                    });
    
                    verificarMedia({
                        id_produto: $("#venderDescProduto").data().id,
                        tipo: "S"
                    }).done(function(data){
                        $("#mediaVenda").text("Média de Venda: " + data.media);
                    });

                    $("#datatableEstoqueProdutos").DataTable().draw(false);
                }
            });
        });

    });
}