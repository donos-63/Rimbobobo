from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("all", views.all),
    path("<str:id>", views.details),
    path("filter_id/<str:id>", views.filter_id),
    path("filter_id/", views.filter_id),
    path("filter_title/<str:text>", views.filter_title),
    path("filter_title/", views.filter_title),
]
