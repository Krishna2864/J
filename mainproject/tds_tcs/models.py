from django.db import models


# MODELS IN TDS MANAGEMENT =>

class tds_client(models.Model):
    tan_no = models.IntegerField()
    department_name = models.CharField(max_length=100)
    mobile_no = models.IntegerField()
    email_id = models.EmailField()
    address = models.CharField(max_length=100)
    trace_username = models.CharField(max_length=50)
    trace_password = models.CharField(max_length=30)

class search_tds(models.Model):
    client_tan_no = models.IntegerField(null=True)
    client_name = models.CharField(max_length=50)
    client_contact_no= models.IntegerField(null=True)
    list_of_client_matches_above_details = models.CharField(max_length=100)

class search_tds_business(models.Model):
    business_name = models.CharField(max_length=50)
    tan_no = models.IntegerField()
    mobile_no=models.IntegerField()
    email_id = models.EmailField()
    address = models.CharField(max_length=70)
    return_type=models.BooleanField(default=False)
    return_for=models.CharField(max_length=20)
    financial_year = models.DateField()
    quarter = models.CharField(max_length=100)
    tds_product = models.CharField(max_length=100)
    coupen_no=models.CharField(max_length=50)
    
class  order_enquiry(models.Model):
    date = models.DateField()
    agent_code = models.CharField(max_length=80)
    category=models.CharField(max_length=20)
    select_product = models.CharField()
    estimated_amount=models.IntegerField()
    quantitiy = models.IntegerField()
    dispatch_need=models.BooleanField(default=False)
    offer_code = models.IntegerField()
    offer_code_discount = models.IntegerField()
    subtotal = models.IntegerField()
    reward_point = models.IntegerField()
    payable_amount_inclusive_tax = models.IntegerField()
    final_amount_after_completation = models.IntegerField()
    select_product = models.CharField(max_length=100)
    remark = models.CharField(max_length=30)


##### tds products
class tds_or_tcs_products(models.Model):
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
