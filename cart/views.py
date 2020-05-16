from django.shortcuts import render, redirect, reverse

def view_cart(request):
    """
    A view that renders the cart contents page
    """
    return render(request, "cart.html", {'cart_page': 'active'})

def add_to_cart(request, id):
    """
    Add a quantity of the specified products to the cart
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
