
from django.shortcuts import render, redirect, get_object_or_404
from .models import Items, Category
from rest_framework import viewsets
from .serializers import CategorySerializer,ItemsSerializer


def index(request):
    cat = Category.objects.all()
    return render(request, 'women/index.html', {'context':cat})

def show_post(request, post_slug):
    post = Items.objects.get(slug=post_slug)

    data = {
        'post': post,
    }

    return render(request, 'women/post.html', data)

def show_category(request, cat_slug):
    cat = Category.objects.get(slug=cat_slug)
    posts = Items.objects.filter(cat_id=cat.pk)

    return render(request, 'women/category.html',{'context':posts})


class CategoryApiView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ItemsApiView(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

