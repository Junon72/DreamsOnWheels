from django.shortcuts import render
from products.models import Product


def index(request):
    """Return the index.html file"""
    products = Product.objects.all()
    context = {
        "index_page": "active",
        "products": products
    }
    return render(request, "index.html", context)