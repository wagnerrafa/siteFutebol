# Generated by Django 2.2.4 on 2019-09-06 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marcar_jogo',
            name='hora',
        ),
    ]
