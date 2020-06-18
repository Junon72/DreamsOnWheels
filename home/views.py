from django.shortcuts import render
from products.models import Product, Original


def index(request):
    """Return the index.html file"""
    products = Product.objects.all()
    highlights = Original.objects.filter(status='h')
    context = {
        "index_page": "active",
        "products": products,
        "highlights": highlights,
        "title": "Home"
    }
    return render(request, "index.html", context)
