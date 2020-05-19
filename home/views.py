from django.shortcuts import render, get_list_or_404
from products.models import Product


def index(request):
    """Return the index.html file"""
    products = get_list_or_404(Product)
    context = {
        "index_page": "active",
        "products": products
    }
    return render(request, "index.html", context)