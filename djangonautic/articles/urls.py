from django.contrib import admin
from . import views
from django.urls import path

app_name = 'articles'

urlpatterns = [
    path("/", views.articles_list, name="list"),
    path("/create/", views.create_article, name="create"),
    path("/<slug:slug>", views.details, name="detail")
]
