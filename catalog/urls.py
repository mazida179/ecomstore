from django.urls import re_path, path
from catalog.views import *


app_name = 'catalog'
urlpatterns = [
    re_path(r"^$", index, name='catalog_home'),

    re_path(r"^category/(?P<category_slug>[-\w]+)/$", show_category, name='catalog_category'),

    # path('category/<slug:category_slug>/', show_category, name='catalog_category'),


    re_path(r"^product/(?P<product_slug>[-\w]+)/$", show_product, name='catalog_product'),

]