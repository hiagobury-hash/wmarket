
export function salvarMovimentacaoEstoque(params) {
    var dfd = new $.Deferred();

    $.ajax({
        url: "salvar_movimentacao_estoque",
        method: "POST",
        data: {
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            id_produto: params.id_produto,
            quantidade: params.quantidade,
            valor: params.valor,
            tipo: params.tipo
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

            if (params.execute){
                params.execute();
            }
        }
    }).done(function (data) {
        dfd.resolve(data);
    });

    return dfd.promise();
}