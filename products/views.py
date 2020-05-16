from django.shortcuts import render
from .models import Product, Original


def all_products(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'sales_page': 'active'
    }
    return render(request, "products.html", context)

# def get_original(request):
