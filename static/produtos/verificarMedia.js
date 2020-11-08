export function verificarMedia(params) {
    var dfd = new $.Deferred();

    $.ajax({
        url: "verificar_media",
        method: "POST",
        data: {
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            id_produto: params.id_produto,
            tipo: params.tipo
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