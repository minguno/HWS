from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    article_list = Article.objects.order_by('-updated_at')
    context = {
        'articles': article_list,
    }
    
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article()
    article.title = title
    article.content = content
    article.save()

    return redirect('articles:index')


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article,
    }

    return render(request, 'articles/detail.html', context)


def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()

    return redirect('articles:index')


def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article,
    }

    return render(request, 'articles/edit.html', context)


def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    new_title = request.POST.get('title')
    new_content = request.POST.get('content')

    article.title = new_title
    article.content = new_content
    article.save()

    return redirect('articles:detail', article.pk)