# Generated by Django 4.0.5 on 2022-07-03 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amigos_panchos', '0007_bebida_foto_burguer_foto_frita_foto_xi_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sobre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(max_length=1200)),
                ('foto', models.ImageField(blank=True, upload_to='fotosSobre/%Y/%m')),
            ],
        ),
    ]
