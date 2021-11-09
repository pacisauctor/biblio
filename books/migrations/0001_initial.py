# Generated by Django 3.2.9 on 2021-11-09 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre del libro')),
                ('author', models.CharField(max_length=75, verbose_name='Autor del libro')),
                ('price', models.FloatField(verbose_name='Precio')),
            ],
        ),
    ]