from django.shortcuts import get_object_or_404
from products.models import Product

def cart_contents(request):
    """
    Make cart contents available regardles which page is being rendered
    """

    cart = request.session.get('cart', {})

    cart_items = []
    totals = 0
    product_count = 0
    

    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        if request.user.is_authenticated:
            total = quantity * product.price
            totals += quantity * product.price
            product_count += quantity
            cart_items.append({'id': id, 'quantity': quantity, 'product': product, 'total': total})
        else:
            if product.old_price > 0:
                total = quantity * product.old_price
                totals += quantity * product.old_price
            else:
                total = quantity * product.price
                totals += quantity * product.price
            product_count += quantity
            cart_items.append({'id': id, 'quantity': quantity, 'product': product, 'total': total})

    return { 'cart_items': cart_items, 'totals': totals, 'product_count': product_count }