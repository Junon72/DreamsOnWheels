from django.shortcuts import render
from .models import Product, Original


def all_products(request):
    products = Product.objects.all()
    context = {
        'login_form': login_form,
        'sales_page': 'active'
    }
    return render(request, "products.html", context)


# def get_highlight(request):
    
