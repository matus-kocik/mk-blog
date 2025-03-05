from django.shortcuts import get_object_or_404, render

from .models import ArticlePage


def article_index(request):
    articles = ArticlePage.objects.all()
    return render(request, "articles/article_index.html", {"articles": articles})


def article_detail(request, slug):
    article = get_object_or_404(ArticlePage, slug=slug)
    return render(request, "articles/article_detail.html", {"article": article})
