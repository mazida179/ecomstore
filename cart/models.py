from django.db import models
from catalog.models import Product

# Create your models here.

class CartItem(models.Model):

    cart_id = models.CharField(max_length=50)
    product = models.ForeignKey(Product, unique=False, on_delete=models.CASCADE)

    date_added = models.DateTimeField(auto_now_add=True)

    quantity = models.IntegerField(default=1)

    class Meta:
        db_table = 'cart_items'
        ordering = ['date_added']
    
    def total(self):
        return self.quantity * self.product.price
    
    def name(self):
        return self.product.name
    
    def price(self):
        return self.product.price
    
    def get_absolute_url(self):
        return self.product.get_absolute_url()
    
    def augment_quantity(self):
        """Increase product quantity by 1"""

        self.quantity = self.quantity + int(1)

        self.save()

