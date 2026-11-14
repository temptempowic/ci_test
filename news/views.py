from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import NewsArticle, Category

def home(request):
    featured_articles = NewsArticle.objects.filter(
        is_published=True, 
        featured=True
    )[:3]
    
    latest_articles = NewsArticle.objects.filter(
        is_published=True
    ).order_by('-published_date')[:6]
    
    categories = Category.objects.all()
    
    context = {
        'featured_articles': featured_articles,
        'latest_articles': latest_articles,
        'categories': categories,
    }
    return render(request, 'news/home.html', context)

def article_list(request):
    articles = NewsArticle.objects.filter(is_published=True).order_by('-published_date')
    
    category_filter = request.GET.get('category')
    if category_filter:
        articles = articles.filter(category__slug=category_filter)
    
    paginator = Paginator(articles, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = Category.objects.all()
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'category_filter': category_filter,
    }
    return render(request, 'news/article_list.html', context)

def article_detail(request, slug):
    article = get_object_or_404(NewsArticle, slug=slug, is_published=True)
    
    related_articles = NewsArticle.objects.filter(
        category=article.category,
        is_published=True
    ).exclude(id=article.id).order_by('-published_date')[:3]
    
    context = {
        'article': article,
        'related_articles': related_articles,
    }
    return render(request, 'news/article_detail.html', context)

def category_articles(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = NewsArticle.objects.filter(
        category=category,
        is_published=True
    ).order_by('-published_date')
    
    context = {
        'category': category,
        'articles': articles,
    }
    return render(request, 'news/category.html', context)
