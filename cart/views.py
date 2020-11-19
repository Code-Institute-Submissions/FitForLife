from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    # The redirect_url is where we came from, we will use this to return to the current page once the user has added items
    redirect_url = request.POST.get('redirect_url')
    product_name = None
    # Debug Code
    for key in request.POST:
        print(key)
        value = request.POST[key]
        print(value)
    if 'product_name' in request.POST:
        product_name = request.POST['product_name']
    # We get the cart variable if it already exists in the session
    # If it exists we return the current cart
    # If it does not exist we return an empty dictionary
    cart = request.session.get('cart', {})

    if product_name:
        if item_id in list(cart.keys()): # we check to see if the item already exists
            if product_name in cart[item_id]['items_by_product_name'].keys():
                cart[item_id]['items_by_product_name'][product_name] += quantity # If it does we increment the quantity
                messages.success(request,
                                 (f'Updated product_name {product_name.upper()} '
                                  f'{product.product_name} quantity to '
                                  f'{cart[item_id]["items_by_product_name"][product_name]}'))
            else:
                cart[item_id]['items_by_product_name'][product_name] = quantity # if it does not exist we initiate a new quantuty
                messages.success(request,
                                 (f'Added product_name {product_name.upper()} '
                                  f'{product.product_name} to your cart'))
        else: # If it does not exist we will create a new cart_items instance
            cart[item_id] = {'items_by_product_name': {product_name: quantity}}
            messages.success(request,
                             (f'Added product_name {product_name.upper()} '
                              f'{product.product_name} to your cart'))
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request,
                             (f'Updated {product.product_name} '
                              f'quantity to {cart[item_id]}'))
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {product.product_name} to your cart')
    # We now update the session with the updated cart
    request.session['cart'] = cart
    # And return to the url we came from
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    product_name = None
    if 'product_product_name' in request.POST:
        product_name = request.POST['product_product_name']
    cart = request.session.get('cart', {})

    if product_name:
        if quantity > 0:
            cart[item_id]['items_by_product_name'][product_name] = quantity
            messages.success(request,
                             (f'Updated product_name {product_name.upper()} '
                              f'{product.product_name} quantity to '
                              f'{cart[item_id]["items_by_product_name"][product_name]}'))
        else:
            del cart[item_id]['items_by_product_name'][product_name]
            if not cart[item_id]['items_by_product_name']:
                cart.pop(item_id)
            messages.success(request,
                             (f'Removed product_name {product_name.upper()} '
                              f'{product.product_name} from your cart'))
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request,
                             (f'Updated {product.product_name} '
                              f'quantity to {cart[item_id]}'))
        else:
            cart.pop(item_id)
            messages.success(request,
                             (f'Removed {product.product_name} '
                              f'from your cart'))

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        product_name = None
        if 'product_product_name' in request.POST:
            product_name = request.POST['product_product_name']
        cart = request.session.get('cart', {})

        if product_name:
            del cart[item_id]['items_by_product_name'][product_name]
            if not cart[item_id]['items_by_product_name']:
                cart.pop(item_id)
            messages.success(request,
                             (f'Removed product_name {product_name.upper()} '
                              f'{product.product_name} from your cart'))
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.product_name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
