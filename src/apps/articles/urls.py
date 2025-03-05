from django.urls import path

from . import views

urlpatterns = [
    path("", views.article_index, name="article_index"),
    path("<slug:slug>/", views.article_detail, name="article_detail"),
]
