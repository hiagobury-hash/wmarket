import { xModal } from "../plugins/xModal/xModal.js";
import { addProduto } from "./addProduto.js";
import { selectDescProduto } from "./selectDescProduto.js";
import { salvarMovimentacaoEstoque } from "./salvarMovimentacaoEstoque.js"
import { verificarEstoque } from "./verificarEstoque.js";
import { verificarMedia } from "./verificarMedia.js";


export function comprarProduto(params) {
    xModal({
        url: 'modal_compra_produtos',
        methods: 'POST',
        frame: 'body',
        idModal: '#modalCompraProdutos'
    }).done(function () {

        $("#btnAddProduto").on("click", function(){
            addProduto();
        });

        selectDescProduto({
            input: "#descProduto",
            execute: function() {
                verificarEstoque({
                    id_produto: $("#descProduto").data().id
                }).done(function(data){
                    $("#saldoCompra").text("Saldo: " + data.saldo);
                });

                verificarMedia({
                    id_produto: $("#descProduto").data().id,
                    tipo: "E"
                }).done(function(data){
                    $("#mediaCompra").text("Média de Compra: " + data.media);
                });
            }
        });

        $("#salvarMovimentacaoEstoque").on("click", function () {
            salvarMovimentacaoEstoque({
                id_produto: $("#descProduto").data().id,
                quantidade:  $("#qtdProduto").val(),
                valor:  $("#vlCompra").val(),
                tipo: 'E',
                execute: function() {
                    verificarEstoque({
                        id_produto: $("#descProduto").data().id
                    }).done(function(data){
                        $("#saldoCompra").text("Saldo: " + data.saldo);
                    });
    
                    verificarMedia({
                        id_produto: $("#descProduto").data().id,
                        tipo: "E"
                    }).done(function(data){
                        $("#mediaCompra").text("Média de Compra: " + data.media);
                    });

                    $("#datatableEstoqueProdutos").DataTable().draw(false);
                }
            });
        });

    });
}
