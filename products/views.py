from django.shortcuts import render


def index(request):
    context = {
        'title': 'главная',
    }
    return render(request, 'products/index.html', context)


def products(request):
    import json
    with open('products/fixtures/prod_list.json') as json_file:
        prod_list = json.load(json_file)
    context = {
        'title': 'продукты',
        'products': prod_list,
    }
    return render(request, 'products/products.html', context)
