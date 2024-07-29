from django.shortcuts import render, get_object_or_404
from catalog.models import *
from django.template import RequestContext
from catalog.forms import ProductAddToCartForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from cart import cart

# Create your views here.
def index(req):
    page_title = 'Musical Instruments and Sheet Music for Musicians'

    req_ctx = RequestContext(req)

    context = locals()

    return render(req, 'catalog/index.html', context)

def show_category(req, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = category.product_set.all()
    page_title = category.name
    meta_keywords = category.meta_keyword

    meta_description = category.meta_description

    req_ctx=RequestContext(req)

    context = locals()

    return render(req, 'catalog/category.html',context)



# Product view, with POST vs GET detection
def show_product(req, product_slug):
    product = get_object_or_404(Product, slug=product_slug)

    categories = product.categories.all()

    page_title = product.name

    meta_keywords = product.meta_keywords

    meta_description = product.meta_description

    req_ctx = RequestContext(req)


    

    # need to evaluate the HTTP method
    if req.method == 'POST':
        # add to cart…create the bound form
        postdata = req.POST.copy()
        
        form = ProductAddToCartForm(req, postdata)

        if form.is_valid():
            print('form data =>', postdata)
            #add to cart and redirect to cart page
            cart.add_to_cart(req)

            # if test cookie worked, get rid of it
            if req.session.test_cookie_worked():
                req.session.delete_test_cookie()
            return HttpResponseRedirect(reverse('show_cart'))
    else:
        # it’s a GET, create the unbound form. Note request as a kwarg
        form = ProductAddToCartForm(request=req)

        # assign the hidden input the product slug
    form.fields['product_slug'].widget.attrs['value'] = product_slug

    # set the test cookie on our first GET request
    req.session.set_test_cookie()

    context = locals()


    return render(req, 'catalog/product.html', context)

