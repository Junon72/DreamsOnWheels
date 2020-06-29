from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import MakePaymentForm, OrderForm
from accounts.forms import UserForm
from django.contrib import messages
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
from accounts.models import Profile
from accounts.forms import ProfileForm
import stripe

@login_required()
def checkout(request):
    '''
    Fetch user profile data to pre-fill
    order form. Provide order form based on 
    profile model and Stripe payment form.
    After successfull transaction, return to
    pack to the Sales page
    '''

    stripe.api_key = settings.STRIPE_SECRET
    publishable = settings.STRIPE_PUBLISHABLE

    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            cart = request.session.get('cart', [])
            total = 0

            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity
                    )
                order_line_item.save()
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(
                    request, "Your card was declined!")

            if customer.paid:
                messages.success(
                    request, "You have successfully paid")
                for id, quantity in cart.items():
                    product = get_object_or_404(Product, pk=id)
                    product.in_stock -= quantity
                    product.save()
                request.session['cart'] = {}
                return redirect(reverse('products:all_products'))
            else:
                messages.error(request, "Unable to take payment")

        else:
            messages.error(
                request,
                "Sorry, there seems to be something wrong with your payment. Please, check the form is filled correctly!"
            )

    else:
        payment_form = MakePaymentForm()
        profile = Profile.objects.get(user=request.user)
        order_form = OrderForm(initial={
            'full_name': profile.user.get_full_name(),
            'email': profile.user.email,
            'phone_number': profile.phone_number,
            'street_address1': profile.address1,
            'street_address2': profile.address2,
            'postcode': profile.zipcode,
            'town_or_city': profile.town_or_city,
            'county': '',
            'country': profile.country,
        })
    context = {
        "order_form": order_form,
        "payment_form": payment_form,
        "publishable": publishable,
        "title": "Checkout",
        "cart": "cart",
    }
    return render(request, "checkout.html", context)
