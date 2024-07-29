from django.shortcuts import render
from django.template import RequestContext
from cart.models import CartItem
from cart import cart


# Create your views here.
def show_cart(req):
    page_title = 'Shopping cart'
    cart_items = cart.get_cart_items(req)
    cart_item_count = cart.cart_distinct_item_count(req)

    req_ctx = RequestContext(req)

    if req.method == 'POST':
        postdata = req.POST.copy()

        if postdata['submit'] == 'Upload':
            cart.update_cart(req)

        if postdata['submit'] == 'Remove':
            cart.remove_from_cart(req)
    
    cart_subtotal = cart.cart_subtotal(req)

    context = locals()
    return render(req, 'cart/cart.html', context)