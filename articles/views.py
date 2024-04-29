from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from . import forms
from .forms import CreateArticle
from .models import Article


# Create your views here.
def articles_list(request):

    articles = Article.objects.all().order_by('date')
    return render(request, 'articles_list.html', {'articles': articles})


def details(request, slug):
    # Retrieve the article with the specified slug from the database
    article = Article.objects.get(slug=slug)
    return render(request, 'article_details.html', {'article': article})

@login_required(login_url='/accounts/login/')
def create_article(request):
    if request.method == 'POST':
        createArticleForm = forms.CreateArticle(request.POST, request.FILES)
        if createArticleForm.is_valid():
            instance = createArticleForm.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('home')
    else:
        createArticleForm = forms.CreateArticle()
    return render(request, 'create_article.html', {'createArticleForm' : createArticleForm})