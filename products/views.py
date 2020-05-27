from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404
from .models import Product, Original
from .filters import ProductFilter


def all_products(request):
    """Get all the Product objects and render them """
    # model = Product
    # template_name = 'products.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
    #     return context
    products = Product.objects.all()
    
    f = ProductFilter(request.GET, queryset=products)
    
    context = {
        # 'products': products,
        'filter': f,
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

