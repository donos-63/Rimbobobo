# Generated by Django 3.2.1 on 2021-05-06 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="content",
            field=models.CharField(
                max_length=5000, verbose_name="Contenu de l'article"
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="title",
            field=models.CharField(max_length=100, verbose_name="Titre"),
        ),
    ]
