# Generated by Django 4.0.5 on 2022-06-28 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amigos_panchos', '0003_cadastrocliente_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]