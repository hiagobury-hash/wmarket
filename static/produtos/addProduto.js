import { xModal } from "../plugins/xModal/xModal.js";

export function addProduto(params) {
    xModal({
        url: 'modal_add_produto',
        methods: 'POST',
        frame: 'body',
        idModal: '#modalAddProduto'
    }).done(function () {

        $("#salvarAddProduto").on("click", function (e) {
            e.preventDefault();
            
            salvarAddProduto({
                descricao: $("#addDescProduto").val(),
                execSuccess: function(){
                    $("#addDescProduto").val("")
                }
            });
        });

    });
}
function salvarAddProduto(params) {
    var dfd = new $.Deferred();

    $.ajax({
        url: "salvar_add_produto",
        method: "POST",
        data: {
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            descricao: params.descricao
        },
        dataType: "json",
        error: function (jqXHR, textStatus, errorThrown) {
            console.log(jqXHR);
        },
        success: function (data) {
            swal({
                title: data.title,
                text: data.msg,
                type: data.status,
                showCancelButton: false,
                confirmButtonColor: '#105BA5',
                confirmButtonText: 'OK',
                allowOutsideClick: false,
                allowEscapeKey: false
            });

            if (params.execSuccess) {
                params.execSuccess();
            }
        }
    }).done(function (data) {
        dfd.resolve(data);
    });

    return dfd.promise();
}