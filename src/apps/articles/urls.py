from django.urls import path

from apps.articles.views import ArticleDetailView, ArticleListView

urlpatterns = [
    path("", ArticleListView.as_view(), name="articles"),
    path("articles/", ArticleListView.as_view(), name="articles"),
    path("<slug:slug>/", ArticleDetailView.as_view(), name="article_detail"),
]
