from django.urls import path, re_path
from .views import *

app_name = 'store'

urlpatterns = [
    re_path(r"^$", home, name='home')
]