from django.shortcuts import render, get_list_or_404
from products.models import Product, Original


def index(request):
    """Return the index.html file"""
    products = get_list_or_404(Product)
    highlights = Original.objects.filter(status='h')
    context = {
        "index_page": "active",
        "products": products,
        "highlights": highlights,
        "title": "Home"
    }
    return render(request, "index.html", context)
