# Generated by Django 3.1.3 on 2020-11-08 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id_produto', models.AutoField(db_column='id_produto', primary_key=True, serialize=False)),
                ('descricao', models.CharField(db_column='descricao', max_length=255)),
                ('dt_cadastro', models.DateTimeField(auto_now_add=True, db_column='dt_cadastro')),
                ('ativo', models.CharField(db_column='ativo', max_length=1)),
            ],
            options={
                'db_table': 'Produtos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MovimentacaoProdutos',
            fields=[
                ('id_movimentacao_produtos', models.AutoField(db_column='id_movimentacao_produtos', primary_key=True, serialize=False)),
                ('quantidade', models.DecimalField(db_column='quantidade', decimal_places=2, max_digits=18)),
                ('valor', models.DecimalField(db_column='valor', decimal_places=2, max_digits=18)),
                ('dt_movimentacao', models.DateTimeField(auto_now_add=True, db_column='dt_movimentacao')),
                ('tipo', models.CharField(blank=True, db_column='tipo', max_length=1, null=True)),
                ('id_produto', models.ForeignKey(db_column='id_produto_fk', on_delete=django.db.models.deletion.PROTECT, to='produtos.produtos')),
            ],
            options={
                'db_table': 'MovimentacaoProdutos',
                'managed': True,
            },
        ),
    ]