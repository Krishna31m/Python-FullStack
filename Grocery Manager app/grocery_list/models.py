from django.db import models

class GroceryItem(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=20)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_purchased = models.BooleanField(default=False)
    purchase_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    store_name = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100)
    email = models.EmailField()
    category = models.CharField(
        max_length=20,
        choices=[
            ('vegetables', 'Vegetables'),
            ('fruits', 'Fruits'),
            ('dairy', 'Dairy'),
            ('bakery', 'Bakery'),
            ('meat', 'Meat'),
            ('snacks', 'Snacks'),
            ('beverages', 'Beverages'),
            ('other', 'Other')
        ],
        default='other'
    )

    def __str__(self):
        return self.item_name