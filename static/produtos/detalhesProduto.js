import { xModal } from "../plugins/xModal/xModal.js";
import { datatableMovimentacaoProduto } from "./datatableMovimentacaoProduto.js";

export function detalhesProduto(params) {
    xModal({
        url: 'modal_detalhes_produto',
        methods: 'POST',
        frame: 'body',
        idModal: '#modalDetalhesProduto'
    }).done(function () {
        $("#detalhesDescProduto").val(params.descricao);
        $("#detalhesEntrada").val(params.entrada);
        $("#detalhesSaida").val(params.saida);
        $("#detalhesSaldo").val(params.saldo);

        datatableMovimentacaoProduto({
            table: "#datatableMovimentacaoProduto",
            id_produto: params.id_produto,
            execute: function(){
                console.log("Teste")
            }
        });
    });
}
