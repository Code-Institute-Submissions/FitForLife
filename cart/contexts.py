from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

# The context processor is responsible for making the contents of the cart available to all application apps
# A context processor has a simple interface:
# it’s a Python function that takes one argument,
# An HttpRequest object, and returns a dictionary that gets added to the template context.
# Each context processor must return a dictionary.

def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    # We first check to see if a cart already exists, if it does not we create an empty dictionary
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id) # Get the product in the bag
            total += item_data * product.price
            product_count += item_data
            # Note that we also add the product object itself so that we can access its image, price, etc
            # when we need to access it throughout the site
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items, # a dictionary of items in the cart
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
