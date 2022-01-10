from django.db import models
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey
from django import forms

  


 ##  models => 





class apply_for_GST_Registration(models.Model):
    MY_CHOICES = ((1,'composition'),(2,'noncomposition'))
    gst_type = models.CharField(max_length=1, choices=MY_CHOICES,default='composition')
    Coupon_No=models.IntegerField(unique=True)
    details_option = ((1,'individual'),(2,'huf'),(3,'Company'),(4,'firm'),(5,'AOP'),(6,'Trust'))
    entitytype = models.CharField(max_length=1,choices=details_option,default='individual')

    business_type = ((1,'Trading'),(2,'Services'))
    nature_of_business = models.CharField(max_length=1,choices=business_type,default='Trading')

    Company_Name=models.CharField(max_length=200)
    Business_Pan_Number=models.CharField(max_length=20,unique=True)
    Mobile_No=models.IntegerField(unique=True)
    State=models.CharField(max_length=100)
    District=models.CharField(max_length=100)
    Address=models.TextField(max_length=200)
    Ward=models.CharField(max_length=50)
    Pin_Code=models.IntegerField(unique=True)
    Annual_Turnover=models.IntegerField()
    Business_Object=models.TextField(max_length=300)
    Same_as_above=models.BooleanField(default=False)
    Name_as_Per_Pan_Card=models.CharField(max_length=50)
    Father_Name=models.CharField(max_length=50)
    DOB=models.DateField()
    Pan_Number=models.CharField(max_length=20,unique=True)
    Aadhar_Number=models.IntegerField(unique=True)
    Mobile_Number=models.IntegerField(unique=True)
    Email_id=models.EmailField(unique=True)
    Member_Pin_code=models.IntegerField(unique=True)
    Member_Address=models.TextField(max_length=200)
    Same_as_above_Authorized=models.BooleanField(default=False)
    Name_as_Per_Pan_Card_Authorized=models.CharField(max_length=50)
    Father_Name_Authorized=models.CharField(max_length=50)
    DOB_Authorized=models.DateField()
    Pan_Number_Authorized=models.CharField(max_length=20,unique=True)
    Aadhar_Number_Authorized=models.IntegerField(unique=True)
    Mobile_Number_Authorized=models.IntegerField(unique=True)
    Email_id_Authorized=models.EmailField(unique=True)
    Member_Pin_code_Authorized=models.IntegerField(unique=True)
    Member_Address_Authorized=models.TextField(max_length=200)

    account_option = ((1,'Saving'),(2,'current'))
    account_type = models.CharField(max_length=1,choices=account_option,default='Saving')
    Account_Holder_Name=models.CharField(max_length=50)
    Account_Number=models.IntegerField(unique=True)
    IFSC_Code=models.CharField(max_length=10)
    Bank_Name=models.CharField(max_length=20)
    Bank_Address=models.TextField(max_length=300)
    Photo=models.ImageField()
    Aadhar_Card=models.ImageField(upload_to='image/')
    Cancel_Cheque=models.ImageField()
    Light_bill=models.ImageField()
    Rent_agreement=models.ImageField()
    Deed_rentagreement_coletter=models.ImageField()
    Authorization_letter=models.ImageField()
    Other_Document=models.ImageField()
    Pancard=models.ImageField()

class GST_Status(models.Model):
    Company_Name=models.CharField(max_length=100)
    Status=models.CharField(max_length=1,choices=((1,'Review'),(2,'Process'),(3,'Pending for ARN'),(4,'Pendig for GST No'),(5,'Review'),(6,'Deliver'),(7,'Cancel'),(8,'Reject')))
    Entity_Type=models.CharField(max_length=1,choices=((1,'Individual'),(2,'HUF'),(3,'Company'),(4,'Firm'),(5,'AOP'),(6,'Trust'),(7,'Other')))
    GST_Type=models.CharField(max_length=1,choices=((1,'Composition'),(2,'non Composition')))
    Coupon=models.CharField(max_length=20)
    Branch_Code=models.CharField(max_length=100)
    Registration_Form=models.CharField(max_length=100)
    Regisration_to=models.CharField(max_length=100)
    GST_NO=models.CharField(max_length=100)
    ARN_NO=models.CharField(max_length=100)
    Form_at=models.CharField(max_length=1,choices=((1,'Branch'),(2,'Taxway')))
    Last_followup_by=models.CharField(max_length=50)

class GST_Return_Client_Details(models.Model):
    Business_Name=models.CharField(max_length=100)
    Type=models.CharField(max_length=100)
    GST_No=models.CharField(max_length=100)
    State=models.CharField(max_length=100)
    Mobile=models.IntegerField()
    Email=models.EmailField()
    Address=models.TextField()
    GST_Portal_Username=models.CharField(max_length=100,unique=True)

class GST_Return_Select_GST_Type(models.Model):
    gst_ty = models.CharField(max_length=1,choices=((1,'composition'),(2,'non_composition')),default='composition')
    GST_typ= models.CharField(max_length=1,choices=((1,'GSTR9 Annual (on NILL) PN 3091',),(2,'GSTR 1'),(3,"GST 1 NILL RETURN"),(4,'GST 10 (GST FINAL RETURN ) for nill data PN 207' )),default='')
 
class view_all_review_gst_form(models.Model):
    coupen_no = models.IntegerField()

class gst_products(models.Model):
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
    types_of_charges = models.CharField(max_length=200)
    terms_conditions = models.TextField(max_length=200)
    faq = models.CharField(max_length=200)
  





 