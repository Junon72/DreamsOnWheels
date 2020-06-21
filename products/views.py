from django.shortcuts import render, get_list_or_404
from .models import Product, Original
from .filters import ProductFilter


def all_products(request):
    """Get all the Product objects and render them """

    products = Product.objects.all()

    f = ProductFilter(request.GET, queryset=products)

    context = {
        'filter': f,
        'sales_page': 'active',
        'title': 'Sales'
    }
    return render(request, "products.html", context)


def get_original(request, id):
    """
    Get a list of Original objects associated with
    the Product
    """

    original = get_list_or_404(Original, id=id)

    context = {
        'original': original,
        'title': 'Original',
    }
    return render(request, "original.html", context)
