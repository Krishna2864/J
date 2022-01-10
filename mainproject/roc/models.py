from django.db import models

class roc(models.Model):
    certificate=models.ImageField(upload_to='image/')
    products_name = models.CharField(max_length=100)
    mrp=models.IntegerField()
    business_amount=models.IntegerField()
    taxable_amount=models.IntegerField()
    tax_amount=models.IntegerField()
    department=models.CharField(max_length=100)
    payment_type = models.IntegerField(default=False)
    coupon_based = models.BooleanField(default=False)
    shipping_quantity = models.IntegerField()
    shipping_amount = models.IntegerField()
    delivery_time = models.DateTimeField()
    Document = models.TextField(max_length=200)
    terms_conditions = models.TextField(max_length=200)
  


