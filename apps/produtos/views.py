from django.shortcuts import render
from apps.produtos.models import (
    Produtos,
    MovimentacaoProdutos,
    MediaProduto
)
from django.http import JsonResponse
from apps.datatable.datatable import DataTableFilter, DataTableRaw
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def index(request):
    return render(request, 'produtos/index.html')


@login_required(login_url='/login/')
def modal_add_produto(request):
    return render(request, 'produtos/modalAddProduto.html')


@login_required(login_url='/login/')
def modal_compra_produtos(request):
    return render(request, 'produtos/modalCompraProdutos.html')


@login_required(login_url='/login/')
def modal_vender_produtos(request):
    return render(request, 'produtos/modalVenderProdutos.html')


@login_required(login_url='/login/')
def modal_detalhes_produto(request):
    return render(request, 'produtos/modalDetalhesProduto.html')


@login_required(login_url='/login/')
def modal_produtos_comprados(request):
    lista = lista_comprados()

    return render(request, 'produtos/modalProdutosComprados.html',{
        'lista': lista
    })


@login_required(login_url='/login/')
def modal_produtos_vendidos(request):
    lista = lista_vendidos()

    return render(request, 'produtos/modalProdutosVendidos.html',{
        'lista': lista
    })


@login_required(login_url='/login/')
def salvar_add_produto(request):
    descricao = request.POST.get("descricao")

    if not descricao:
        data = {
            "title": "Erro!",
            "status": "error",
            "msg": "Descrição é um campo obrigatório"
        }

        return JsonResponse(data, safe=False)

    exists = Produtos.objects.filter(
        descricao=descricao
    ).exists()

    if not exists:
        fs = Produtos()
        fs.descricao = descricao
        fs.ativo = 'S'
        fs.save()

        data = {
            "title": "Sucesso!",
            "status": "success",
            "msg": "Produto adicionado com sucesso!"
        }
    else:
        data = {
            "title": "Erro",
            "status": "error",
            "msg": "Produto já está cadastrado!"
        }

    return JsonResponse(data, safe=False)


@login_required(login_url='/login/')
def select_desc_produto(request):
    descricao = request.POST.get('descricao', '')

    items = Produtos.objects.filter(
        descricao__contains=descricao
    )
    data = list()

    for item in items:
        data.append({
            'id': item.id_produto,
            'text': item.descricao
        })

    return JsonResponse(data, safe=False)


@login_required(login_url='/login/')
def salvar_movimentacao_estoque(request):
    id_produto = request.POST.get('id_produto')
    quantidade = request.POST.get('quantidade').replace(",", ".")
    valor = request.POST.get('valor').replace(",", ".")
    tipo = request.POST.get('tipo')

    if not id_produto or not quantidade or not valor or not tipo:
        data = {
            "title": "Erro!",
            "status": "error",
            "msg": "Todos os campos são obrigatórios"
        }

        return JsonResponse(data, safe=False)

    if float(quantidade) <= 0 or float(valor) <= 0:
        data = {
            "title": "Erro!",
            "status": "error",
            "msg": "Quantidade e Valor não podem ser 0"
        }

        return JsonResponse(data, safe=False)

    items = MovimentacaoProdutos.objects.filter(
        id_produto=id_produto
    )

    estoque = calcular_estoque(id_produto, tipo, quantidade)

    print(estoque)
    
    if estoque >= 0:
        fs = MovimentacaoProdutos()
        fs.id_produto_id = id_produto
        fs.quantidade = quantidade
        fs.valor = valor
        fs.media_compra = 0
        fs.tipo = tipo
        fs.save()

        fs = MediaProduto()
        fs.id_produto_id = id_produto
        fs.tipo = tipo
        fs.valor = calcular_media(id_produto, tipo)
        fs.save()

        data = {
            "title": "Sucesso",
            "status": "success",
            "msg": "Produto movimentado com sucesso!"
        }

    else:
        
        data = {
            "title": "Erro",
            "status": "error",
            "msg": "O estoque do produto não pode ser menor que 0"
        }

    return JsonResponse(data, safe=False)

def calcular_estoque(id_produto, tipo, quantidade):
    items = MovimentacaoProdutos.objects.filter(
        id_produto=id_produto
    )

    total = 0
    for item in items:
        if item.tipo == 'E':
            total = float(total) + float(item.quantidade)
        elif item.tipo == 'S':
            total = float(total) - float(item.quantidade)

    if tipo == 'E':
        return total + float(quantidade)
    elif tipo == 'S':
        return total - float(quantidade)


def calcular_media(id_produto, tipo):
    items = MovimentacaoProdutos.objects.filter(
        id_produto=id_produto,
        tipo=tipo
    )

    media = 0
    total = 0
    total_valor = 0
    total_quantidade = 0
    for item in items:
        total_quantidade = float(total_quantidade) + float(item.quantidade)
        total = total + (float(item.valor) * float(item.quantidade))

    media = total / total_quantidade

    return float(media)


@login_required(login_url='/login/')
def verificar_estoque(request):
    id_produto = request.POST.get("id_produto")

    items = MovimentacaoProdutos.objects.filter(
        id_produto=id_produto
    )

    total = 0
    for item in items:
        if item.tipo == 'E':
            total = float(total) + float(item.quantidade)
        elif item.tipo == 'S':
            total = float(total) - float(item.quantidade)

    data = {
        "saldo": total
    }

    return JsonResponse(data, safe=False)


@login_required(login_url='/login/')
def verificar_media(request):
    id_produto = request.POST.get("id_produto")
    tipo = request.POST.get("tipo")

    media = 0
    item = MediaProduto.objects.filter(
        id_produto=id_produto,
        tipo=tipo
    ).latest('id_media_produto')
    if item:
        media = item.valor

    data = {
        "media": media
    }

    return JsonResponse(data, safe=False)


def lista_comprados():
    items = MovimentacaoProdutos.objects.filter(
        tipo="E"
    )

    data = list()

    for item in items:

        media = MediaProduto.objects.filter(
            id_produto=item.id_produto_id,
            tipo="E"
        ).latest('id_media_produto')

        data.append({
            "descricao": item.id_produto.descricao,
            "quantidade": item.quantidade,
            "valor": item.valor,
            "media": media.valor
        })

    return data


def lista_vendidos():
    items = MovimentacaoProdutos.objects.filter(
        tipo="S"
    )

    data = list()

    for item in items:
        media = MediaProduto.objects.filter(
            id_produto=item.id_produto_id,
            tipo="S"
        ).latest('id_media_produto')

        data.append({
            "descricao": item.id_produto.descricao,
            "quantidade": item.quantidade,
            "valor": item.valor,
            "media": media.valor
        })

    return data

@login_required(login_url='/login/')
def datatable_produtos(request):

        columns = list()
        columns = [
            {
                'cl': 'id_produto',
                'type': 'str'
            },
            {
                'cl': 'descricao',
                'type': 'str'
            },
        ]

        where = {}

        order = [
            'id_produto',
        ]

        datatable = DataTableFilter(request, Produtos, columns, where, order)

        return JsonResponse(datatable.data, safe=False, json_dumps_params={'indent': 2})


@login_required(login_url='/login/')
def datatable_movimentacao_produto(request):

        id_produto = request.POST.get("id_produto", None)

        columns = list()
        columns = [
            {
                'cl': 'tipo',
                'type': 'str'
            },
            {
                'cl': 'quantidade',
                'type': 'str'
            },
            {
                'cl': 'dt_movimentacao',
                'type': 'date'
            },
        ]

        where = {
            'id_produto': id_produto
        }

        order = [
            'dt_movimentacao',
        ]

        datatable = DataTableFilter(request, MovimentacaoProdutos, columns, where, order)

        return JsonResponse(datatable.data, safe=False, json_dumps_params={'indent': 2})


@login_required(login_url='/login/')
def datatable_estoque_produtos(request):

    columns = list()
    columns = [
        'descricao',
        'entrada',
        'saida',
        'saldo',
        'id_produto_id'
    ]

    query = '''
       SELECT * FROM v_estoque_produtos
    '''

    where = None

    value_where = []

    group_by = None

    datatable = DataTableRaw(request, MovimentacaoProdutos, columns, query, where, value_where, group_by)

    return JsonResponse(datatable.data, safe=False, json_dumps_params={'indent': 2})