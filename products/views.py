from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404
from .models import Product, Original


def all_products(request):
    """Get all the Product objects and render them """
    
    products = Product.objects.all()
    context = {
        'products': products,
        'sales_page': 'active'
    }
    return render(request, "products.html", context)

def get_original(request, id):
    """
    Get a list of Original objects associated with 
    the Product
    """

    original = get_list_or_404(Original, id=id)
    return render(request, "original.html", {'original': original})
