"""
URL configuration for news app.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
"""
from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/', views.article_list, name='article_list'),
    path('category/<slug:slug>/', views.category_articles, name='category'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
]
