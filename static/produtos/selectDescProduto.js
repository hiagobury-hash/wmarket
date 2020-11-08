export function selectDescProduto(params) {
    var dfd = new $.Deferred();

    $(params.input).data({
        input: params.input,
        id: params.id,
        descricao: params.descricao
    });

    var dados = $(params.input).data();

    $(params.input).select2({
        minimumInputLength: 0,
        placeholder: "Filtrar",
        allowClear: true,
        ajax: {
            url: "select_desc_produto",
            dataType: 'json',
            type: "POST",
            data: function (val) {
                return {
                    csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
                    descricao: val.term
                };
            },
            processResults: function (data) {
                return {
                    results: data
                };
            }
        }
    });

    $(params.input).on("select2:selecting", function (e) {
        $.extend(dados, {
            id: e.params.args.data.id,
            descricao: e.params.args.data.text
        });

        if(params.execute){
            params.execute();
        }
        
    });

    $(params.input).on("select2:clear", function (e) {
        $.extend(dados, {
            id: null,
            descricao: ''
        });
        $(params.input).val(0).trigger('change');

    });

    dfd.resolve();

    return dfd.promise();
}