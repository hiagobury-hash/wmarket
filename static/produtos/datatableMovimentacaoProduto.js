export function datatableMovimentacaoProduto(params) {
    var dfd = new $.Deferred();

    var table = params.table;

    $(table).DataTable().destroy();

    $(table).DataTable({
        dom: 'l<"toolbar">rt<"panel-footer"ip>',
        aLengthMenu: [
            [15, 25, 50, 100, 9000000],
            [15, 25, 50, 100, "Todos"]
        ],
        processing: true,
        serverSide: true,
        responsive: false,
        ordering: true,
        order: [],
        ajax: {
            url: 'datatable_movimentacao_produto',
            type: "POST",
            data: {
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
                id_produto: params.id_produto
            },
            error: function (data) {
                console.log(data);
            }
        },
        createdRow: function (row, data) {
            $(row).addClass('disable-select');
            $(row).addClass('tr_select');
            $(row).addClass('cursor-pointer');
            if(data[0] ==  'E'){
                $(row).css('color', 'rgba(12, 196, 107)');
            }
            if(data[0] ==  'S'){
                $(row).css('color', 'rgba(196, 12, 12)');
            }
        },
        initComplete: function (settings) {
            var api = this.api();
            params.execute(api);
            dfd.resolve();
        },
        rowCallback: function (row, data) {
            if (params.rowCallback) {
                params.rowCallback(row, data);
            }
        }
    });

    var datatable = $(table).DataTable();

    $(table + ' thead tr:eq(1) td').each(function () {
        var title = $(table + ' thead tr:eq(0) th').eq($(this).index()).text();

        $(this).html('<input class="form-control individual_filter" type="text" placeholder="Filtrar ' + title + '" />');
        
    });

    datatable.columns().every(function () {
        var that = this;

        $('.individual_filter', table + ' thead tr:eq(1) td').eq(this.index()).on('change', function () {
            if (that.search() !== this.value) {
                that.search(this.value).draw();

            }
        });
        
    });

    $('.dataTables_length select').addClass("form-control");

    return dfd.promise();
}