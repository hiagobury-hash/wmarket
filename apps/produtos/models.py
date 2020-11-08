from django.db import models

class Produtos(models.Model):
    id_produto = models.AutoField(
        db_column='id_produto', primary_key=True)
    descricao = models.CharField(
        db_column='descricao', max_length=255, blank=False, null=False)
    dt_cadastro = models.DateTimeField(
        db_column='dt_cadastro', auto_now_add=True, blank=False, null=False)
    ativo = models.CharField(
        db_column='ativo', max_length=1, blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'Produtos'

    def __str__(self):
        return self.descricao

class MovimentacaoProdutos(models.Model):
    id_movimentacao_produtos = models.AutoField(
        db_column='id_movimentacao_produtos', primary_key=True)
    id_produto = models.ForeignKey(
        Produtos, db_column='id_produto_fk', on_delete=models.PROTECT, blank=False, null=False)
    quantidade = models.DecimalField(
        db_column='quantidade', max_digits=18, decimal_places=2, blank=False, null=False)
    valor = models.DecimalField(
        db_column='valor', max_digits=18, decimal_places=2, blank=False, null=False)
    dt_movimentacao = models.DateTimeField(
        db_column='dt_movimentacao', auto_now_add=True, blank=False, null=False)
    tipo = models.CharField(
        db_column='tipo', max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'MovimentacaoProdutos'

    def __str__(self):
        return self.id_produto.descricao

class MediaProduto(models.Model):
    id_media_produto = models.AutoField(
        db_column='id_media_produto', primary_key=True)
    id_produto = models.ForeignKey(
        Produtos, db_column='id_produto_fk', on_delete=models.PROTECT, blank=False, null=False)
    valor = models.DecimalField(
        db_column='valor', max_digits=18, decimal_places=2, blank=False, null=False)
    dt_media = models.DateTimeField(
        db_column='dt_media', auto_now_add=True, blank=False, null=False)
    tipo = models.CharField(
        db_column='tipo', max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'MediaProduto'

    def __str__(self):
        return self.id_produto.descricao