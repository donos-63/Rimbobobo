from django.db import models


class Article(models.Model):
    title = models.CharField("Titre", max_length=100)
    description = models.CharField("Description", max_length=100)
    content = models.CharField("Contenu de l'article", max_length=5000)
    end_date = models.DateTimeField("Date de fin de parution")
    is_adm_only = models.BooleanField("administrator visibility only", default=True)
