export function verificarEstoque(params) {
    var dfd = new $.Deferred();

    $.ajax({
        url: "verificar_estoque",
        method: "POST",
        data: {
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            id_produto: params.id_produto
        },
        dataType: "json",
        error: function (jqXHR, textStatus, errorThrown) {
            console.log(jqXHR);
        },
    }).done(function (data) {
        dfd.resolve(data);
    });

    return dfd.promise();
}