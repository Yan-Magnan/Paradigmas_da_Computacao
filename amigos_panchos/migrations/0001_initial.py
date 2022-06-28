# Generated by Django 4.0.5 on 2022-06-28 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cadastroCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='nome')),
                ('telefone', models.CharField(max_length=200, verbose_name='telefone')),
                ('dataNascimento', models.CharField(max_length=200, verbose_name='dataNascimento')),
                ('cep', models.CharField(max_length=200, verbose_name='cep')),
                ('senha1', models.CharField(max_length=200, verbose_name='senha1')),
                ('rua', models.CharField(max_length=200, verbose_name='rua')),
                ('numero', models.CharField(max_length=200, verbose_name='numero')),
                ('bairro', models.CharField(max_length=200, verbose_name='bairro')),
                ('cidade', models.CharField(max_length=200, verbose_name='cidade')),
                ('senha2', models.CharField(max_length=200, verbose_name='senha2')),
            ],
        ),
    ]