(function ($) {
    $.fn.DataTableEdit = function () {

        fn = this;

        return methods.init(fn);
    };

    var methods = {
        init: function (fn) {

            //var data = $(fn).parent().parent().DataTable().row(fn).data();
            $(fn).on('dblclick', 'tbody tr td', function (e) {
                var data = $(fn).DataTable().row($(this).parents('tr')).data();
                
                id = data[2];
                descricao = data[0];

                $(this).empty();

                $(this).append("<form><input id='descricao_salvar' type='text' class='form-control' /></form>");

                $("#descricao_salvar").val(descricao);

                $("#descricao_salvar").focus();

                $("#descricao_salvar").on("blur", function(){
                    $(fn).DataTable().draw(false);
                });

                methods.descricao_salvar(fn, id);
            });
        },

        descricao_salvar: function (fn, id) {
            $('form #descricao_salvar').keydown(function (e) {
                if (e.keyCode == 13) {
                    e.preventDefault();
                    
                    $("#descricao_salvar").off("blur");
        
                    var dfd = new $.Deferred();
                    $.ajax({
                        url: "/ensaio/salvar_editar_parametro_opcao",
                        method: "POST",
                        data: {
                            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
                            id_parametro_opcao: id,
                            descricao: $(this).val()
                            
                        },
                        dataType: "json",
                        error: function (jqXHR, textStatus, errorThrown) {
                            console.log(jqXHR);
                        }
                    }).done(function (data) {
        
                        $(fn).DataTable().draw(false);
        
                        dfd.resolve(data);
                    });
        
                    return dfd.promise();
                }
            });
        },
    };

})(jQuery);
/*

DataTableEdit: function(fn, that){
    descricao = $(fn).DataTable().cell(that).data();

    var data = $(fn).DataTable().row($(that).parents('tr')).data();

    dados.id_parametro = data[2]

    $(that).empty();

    $(that).append("<form><input id='descricao_salvar' type='text' class='form-control' /></form>");

    $("#descricao_salvar").val(descricao);

    $("#descricao_salvar").focus();

    $("#descricao_salvar").on("blur", function(){
        $(fn).DataTable().draw(false);
    });

    methods.descricao_salvar(fn);
},



*/