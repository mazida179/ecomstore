from django.urls import re_path
from cart.views import *

urlpatterns = [
    re_path(r"^$", show_cart, name='show_cart' ),
]