from django.views.generic import DetailView, ListView

from .models import ArticlePage


class ArticleListView(ListView):
    model = ArticlePage
    template_name = "articles/articles.html"
    context_object_name = "articles"
    queryset = ArticlePage.objects.all().order_by("-date_published")


class ArticleDetailView(DetailView):
    model = ArticlePage
    template_name = "articles/article.html"
    context_object_name = "article"
