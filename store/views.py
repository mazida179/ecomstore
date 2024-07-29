from django.shortcuts import render
from catalog.models import Product

# Create your views here.
def home(req):
    products = Product.objects.all()
    context = locals()
    return render(req, 'index.html', context)