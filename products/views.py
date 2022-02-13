from django.shortcuts import render
from products.models import Product, ProductCategory


def index(request):
    context = {
        'title': 'главная',
    }
    return render(request, 'products/index.html', context)


def products(request):
    all_products = Product.objects.all()
    categories = ProductCategory.objects.all()
    context = {
        'title': 'продукты',
        'products': all_products,
        'categories': categories,
    }
    return render(request, 'products/products.html', context)

