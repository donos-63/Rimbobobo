# Generated by Django 3.2.1 on 2021-05-06 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titre')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('content', models.CharField(max_length=1000, verbose_name="Contenu de l'article")),
                ('end_date', models.DateTimeField(verbose_name='Date de fin de parution')),
                ('is_adm_only', models.BooleanField(default=True, verbose_name='administrator visibility only')),
            ],
        ),
    ]
