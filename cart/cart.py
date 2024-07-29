from catalog.models import Product
from cart.models import CartItem
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
import decimal, random


CART_ID_SESSION_KEY = 'cart_id'

# Get the current user's cart id, set the new one if blank.

def _cart_id(req):
    """
    Get the current user's cart id, set the new one if blank.
    """
    if req.session.get(CART_ID_SESSION_KEY, '') == '':
        req.session[CART_ID_SESSION_KEY] = _generate_cart_id()
    return req.session[CART_ID_SESSION_KEY]
    

def _generate_cart_id():
    cart_id = ''
    characters = 'ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvxyz1234567890!@#$%^&*()'
    cart_id_lenght = 50

    for _ in range(cart_id_lenght):
        cart_id += characters[random.randint(0, len(characters)-1)]
    return cart_id

# return all items from the current user's cart
def get_cart_items(req):
    """
    Returns all items from the current user's cart
    """
    return CartItem.objects.filter(cart_id = _cart_id(req))

# add an item to the cart
def add_to_cart(req):
    """
    Adds to cart
    """

    postdata = req.POST.copy()

    # get product slug from post data, return blank if empty
    product_slug = postdata.get('product_slug', '')

    # get quantity added, return 1 if empty
    quantity = postdata.get('quantity', 1)

    # fetch the product or return a missing page error
    product = get_object_or_404(Product, slug=product_slug)

    #get products in cart
    cart_products = get_cart_items(req)

    product_in_cart = False

    # check to see if item is already in cart
    for cp in cart_products:
        if cp.product.id == product.id:
            # update the quantity if found
            cp.augment_quantity()
            product_in_cart = True

    if not product_in_cart:
        # create and save a new cart item
        ci = CartItem()
        ci.product = product
        ci.quantity = quantity
        ci.cart_id = _cart_id(req)
        ci.save()

# returns the total number of items in the user's cart
def cart_distinct_item_count(req):
    return get_cart_items(req).count()


# gets the total cost for the current cart
def cart_subtotal(req):
    cart_total = decimal.Decimal(0.00)

    cart_products = get_cart_items(req)

    for cart_item in cart_products:
        cart_total += cart_item.product.price * cart_item.quantity
    return cart_total


def get_single_item(req, item_id):
    return get_object_or_404(CartItem, id = item_id, cart_id = _cart_id(req))


# Remove a single item from cart
def remove_from_cart(req):
    postdata = req.POST.copy()

    item_id = postdata['item_id']

    cart_item = get_single_item(req, item_id)

    if cart_item:
        cart_item.delete()


# Update quantity for single item
def update_cart(req):
    postdata = req.POST.copy()

    item_id = postdata['item_id']

    quantity = postdata['quantity']

    cart_item = get_single_item(req, item_id)

    if cart_item:
        if int(quantity) > 0:
            cart_item.quantity = int(quantity)
            cart_item.save()
        else:
            remove_from_cart(req)

