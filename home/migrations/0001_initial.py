# Generated by Django 2.2.4 on 2019-09-05 02:19

import ckeditor.fields
import ckeditor_uploader.fields
import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marcar_Jogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
                ('end', models.CharField(max_length=255)),
                ('tel', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('hora', models.CharField(max_length=255)),
                ('lugar', models.CharField(choices=[('G', 'Gramado'), ('S', 'Society'), ('F', 'Futsal'), ('T', 'Taqueada')], max_length=255)),
                ('msg', models.CharField(max_length=255)),
                ('criado', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('resumo', ckeditor.fields.RichTextField()),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('author', models.CharField(max_length=255)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='imagem')),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
