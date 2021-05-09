# Rimbobobo

## Pré requis
* installer le [requirement.txt](requirements.txt)

## Exécution
* vscode (launch.json fournit pour le débuggage vscode)
* en ligne de commande:
     ``` python
     python manage.py runserver
     ```

## Fonctionnalités
### Homepage
![admin](screenshot/admin.png)
* Les articles s'administrent dans [la page admin](http://127.0.0.1:8000/admin/) . Le login / passowrd a été fournit dans simplonline
  * CRUD sur les articles
  * Création de users et affectation des privilèges
 
---

### Homepage
![admin](screenshot/home.png)
* Affichage des articles [ici](http://127.0.0.1:8000/all/):
  * affichage des articles non perimés (end_date<today > __lt vs __lte c'est maitrisé!)
  * affichage des articles resérvés aux admins si session admin ouverte
 
---

### Recherches
* Recherche un article:
    * filtre par id ou alors recherche partielle dans le titre de l'article. 
    * pour une recherche dans le titre, au moins 3 caractères!
    * Si pas de match, pas de résultat. Si filtre vide, tous les résultats
 
---

### Recherche par ID
![admin](screenshot/search2.png)
 
---

### Recherche par Titre
![admin](screenshot/search.png)

---

## technique
* base de donnée hebergée sur [ElephantSQL](https://www.elephantsql.com/)

---

## Azure
* pas de compte, pas de déploiement
