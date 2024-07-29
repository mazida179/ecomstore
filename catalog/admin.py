from django.contrib import admin
from catalog.models import *
from catalog.forms import *

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
# sets values for how the admin site lists your products
    list_display = ('name', 'price', 'old_price', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-created_at']    
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ('created_at', 'updated_at',)
    # sets up slug to be generated from product name

    """
    prepopulated_fields variable you set up in your admin class for each model. With this setting in place,
    your admin interface will convert anything you enter in the title and convert it to all lowercase letters, as
    well as translate any spaces or URL-illegal characters to dashes.
    """
    prepopulated_fields = {'slug' : ('name',)}


# Register Product table in the Admin.    
admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ('created_at', 'updated_at',)
    # sets up slug to be generated from category name
    prepopulated_fields = {'slug' : ('name',)}


admin.site.register(Category, CategoryAdmin)