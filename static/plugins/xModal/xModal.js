export function xModal(params){
    var dfd = new $.Deferred();

    $.ajax({
        url: params.url,
        method: params.method,
        data: params.data,
        error: function(jqXHR, textStatus, errorThrown) {
            params.error(jqXHR);
        }
    }).done(function(data) {
        $(params.frame).append(data);

        openModal(params.idModal);
        closeModal(params.idModal);
        
        dfd.resolve(data);
    });

    return dfd.promise();
}

function openModal(idModal){
    $(idModal).modal("show");
    $('.money').mask("#.##0,00", {reverse: true});
    $('.number').mask("#.##0.00", {reverse: true});
}

function closeModal(idModal){
    $(idModal).on('hidden.bs.modal', function () {
        $(idModal).remove();
    });
}