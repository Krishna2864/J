from django.db import models
from django import forms

class personal_info(models.Model):

    Pan_number = models.IntegerField()
    surname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    firstname = models.CharField(max_length=20)
    password = models.CharField(max_length=100,default='1234567890')
    DOB = models.DateField()
    father_name = models.CharField(max_length=100)
    aadhar_no = models.IntegerField()
    adhar_enrollment_id = models.IntegerField()
    gender  = models.BooleanField(default= True)
    name_of_premises_building_village = models.CharField(max_length=100)
    flat_door_building = models.CharField(max_length=100)
    area_locality = models.CharField(max_length=100)
    town_city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    Pin_code = models.IntegerField()
    land_line = models.IntegerField()
    primary_mobile_no = models.IntegerField()
    secondary_mobile_number = models.IntegerField()
    primary_email_id = models.EmailField()
    secondary_email_id = models.EmailField()
    bank_ifsc_code = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    contact_type = models.CharField(max_length=100)
    account_type = models.CharField(max_length=100)
    account_no = models.IntegerField()
    bank_ifsc_code_2 = models.CharField(max_length=100)
    bank_name_2 = models.CharField(max_length=100)
    account_no_2 = models.IntegerField()


class itr_type(models.Model):
    select_itr_type = models.CharField(max_length=100)
    assesment_year = models.DateField()
    return_type = models.CharField(max_length=100)
    select_acknowlegement_no = models.IntegerField()
    original_return_date = models.DateField()


class itrform(models.Model):
    Pan_number = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    assesment_year = models.CharField(max_length=100)
    income_from_salary = models.CharField(max_length=100)
    income_from_house_property = models.CharField(max_length=100)
    income_from_other_sources = models.CharField(max_length=100)
    capital_gain = models.CharField(max_length=100)
    exempted_income = models.CharField(max_length=100)
# deductions
    c_80 = models.IntegerField()
    g_80 = models.IntegerField()
    other_deductions = models.IntegerField()
    gga_80 = models.IntegerField()
    d_80 = models.IntegerField()

    gross_total_deductions = models.IntegerField()
    net_taxable_income = models.IntegerField()

# taxes paid
    tds_on_salary = models.IntegerField()
    non_salary_tds = models.IntegerField()
    tcs_entry_tax_collected_at_source = models.IntegerField()
    advance_tax_or_self_assesment_tax= models.IntegerField()
    tds_tax_deducted_at_source_16_c = models.IntegerField()  
    total_tax = models.IntegerField()

# schedule

    schedule_di = models.CharField(max_length=100)\

#  show details amount , get the info from form
# amount 1
    amount1 = models.IntegerField()
    amount2 = models.IntegerField()
    amount3 = models.IntegerField()
    amount4 = models.IntegerField()
    amount5 = models.IntegerField()
    amount6 = models.IntegerField()
    addition = models.IntegerField()

# amount 2
    amount1 = models.IntegerField()
    amount2 = models.IntegerField()
    amount3 = models.IntegerField()
    amount4 = models.IntegerField()
    amount5 = models.IntegerField()
    amount6 = models.IntegerField()
    addition = models.IntegerField()

# amount 3
    amount1 = models.IntegerField()
    amount2 = models.IntegerField()
    amount3 = models.IntegerField()
    amount4 = models.IntegerField()
    amount5 = models.IntegerField()
    amount6 = models.IntegerField()

# amount 4
    amount1 = models.IntegerField()
   
# upload attachments

    Pancard=models.ImageField(upload_to='image/')
    previous_itr_if_available=models.ImageField(upload_to='image/')
    form_16_a_attachment=models.ImageField(upload_to='image/')
    balance_sheet=models.ImageField(upload_to='image/')
    loan_or_investment=models.ImageField(upload_to='image/')
    Aadhar_Card=models.ImageField(upload_to='image/')
    form_16_attachment=models.ImageField(upload_to='image/')
    other_attachment=models.ImageField(upload_to='image/')
    tac_saving_docs_atachment=models.ImageField(upload_to='image/')


#####
class income_from_capital(models.Model):
    types_of_property = models.CharField(max_length=1,choices=((1,'Land'),(2,'Building'),(3,'Land and Building (Both)')),default='Other')
    date_of_sale = models.DateField(default='')
    sale_price = models.IntegerField()
    date_of_purchase= models.DateField(default='')
    purchase_price = models.IntegerField()
    selling_expenses_like_brokerage = models.IntegerField()
    cost_of_improvemet = models.IntegerField(default=0)
    date_of_improvement = models.DateField()


#####
class exempted_income(models.Model):
    exempted_income_head_list = ((1,'Agricuture Income (=<5000)'),(2,'Any amount from the central/state Govt/local authority by way of compensation on account of any disaster'),(3,'Any sum received under a life insurance policy, includig the sum allocated by way of bonus on such policy'),
    (4,'Statuory Provident Fund received'),(4,'Recognised Provident Fund received'),(5,'Scholarships granted to meet the cost of education'),(6,'Approved superannuation fund received'),
    (7,'Allowance MP/MLA/MLC'),(8,'Award instituted by Government'),(9,'Pension received by inner of "param vir chakra" or "maha vir chakra " or "vir chakra" or such other'),(10,'Defense medical disability pension'),(10,'armed forces family pension in case of death during operational duty'),(11,'Any income as referred to in sectio 10(26)'),
    (12,'Any income as referred to in section 10(26AAA)'),(13,'Exempted Dividend Income'),(14,'Any Other'))
    exempted_income_head = models.CharField(max_length=1,choices=exempted_income_head_list,default='Any Other')
    exempted_income_description = models.CharField(max_length=1)
    amount = models.IntegerField()

class professional_income(models.Model):
    professional_service_name = models.CharField(max_length=100)
    type_of_profession = models.CharField(max_length=100)
    gross_receipt = models.CharField(max_length=100)
    net_profit_more_than_50p_of_gr = models.CharField(max_length=100)
    partner_members = models.CharField(max_length=100)
    secured_loans = models.CharField(max_length=100)
    unsecured_loans = models.CharField(max_length=100)
    advances = models.CharField(max_length=100)
    sundry_creditors = models.CharField(max_length=100)
    other_liability= models.CharField(max_length=100)
    total_capital_and_liabilities = models.CharField(max_length=100)
    fixed_assests = models.CharField(max_length=100)
    invetories = models.CharField(max_length=100)
    sundry_debtors = models.CharField(max_length=100)
    balance_with_banks_as_on_31_03_2021 = models.CharField(max_length=100)
    cash_in_hand = models.CharField(max_length=100)
    loan_and_advances = models.CharField(max_length=100)
    other_assests = models.CharField(max_length=100)
    total_assests = models.CharField(max_length=100)


class import_tds(models.Model):
    income_chargeable_under_the_head_salaeies=models.CharField(max_length=100)
    name_of_the_employer  = models.CharField(max_length=100)
    tan_of_the_employer  = models.CharField(max_length=100)
    employer_type  = models.CharField(max_length=1,choices=((1,'government'),(2,'public sector unit'),(3,'private'),(4,'other')))
    tax_deducted_on_salarry  = models.CharField(max_length=100)
    address_line = models.CharField(max_length=100)
    town_city  = models.CharField(max_length=100)
    state  = models.CharField(max_length=100)
    Pin_code  = models.IntegerField()

y = 'tanvi'
#1

class Income_From_Salary_Pension(models.Model):
    Name_of_Employer_or_Company=models.CharField(max_length=50)
    Address=models.TextField(max_length=200)
    types_of_employer = models.CharField(max_length=1,choices=((1,'Central Goverment'),(2,'State Government'),(3,'Public Sector Undertaking'),
    (4,'Pensioners'),(5,'Others'),(6,'Private'),(7,'Not Applicable'),(8,"public sector unit")))
    Salary_or_Pension_or_Allowances=models.IntegerField()
    Values_of_perquisites=models.IntegerField()
    Profit_in_lieu_of_salary=models.IntegerField()
    Gross_Salary=models.IntegerField()
    Other_Exempt_Allowances_if_any_subtract=models.IntegerField()
    Standard_Deductions_subtract=models.IntegerField()
    Entertainment_Allowances_subtract=models.IntegerField()
    Professional_Tax_subtract=models.IntegerField()
    Income_Charge_under_the_head_salaries=models.IntegerField()
    Basic_Salary=models.IntegerField()
    HRA=models.IntegerField()
    Rent_Paid=models.IntegerField()

class Income_From_House_Property(models.Model):
    Type_of_House_Property=models.CharField(max_length=1,choices=((1,'Self Ocupied'),(2,'Let Out'),(3,'Demed Let Out')))
    Address=models.TextField(max_length=200)
    Gross_Rent_Recieved_or_Receivable_or_Letable_Value=models.IntegerField()
    Tax_Paid_to_local_authorities=models.IntegerField()
    Annual_Values=models.IntegerField()
    Annual_Value_of_30_percent=models.IntegerField()
    Interest_Payable_on_Home_Loan=models.IntegerField()
    Income_chareable_under_the_head_House_Property=models.IntegerField()

class Income_from_Other_Sources(models.Model):
    Income_from_Tution=models.IntegerField()
    Interest_from_Saving_Bank=models.IntegerField()
    Interest_from_FD=models.IntegerField() 
    Interest_from_Income_Tax_Refund=models.IntegerField() 
    Other_party_Interest=models.IntegerField() 
    Income_from_commission=models.IntegerField() 
    Income_from_dividend_Other_than_indian_company=models.IntegerField() 
    Deduction_In_case_of_family_pension_only=models.IntegerField() 
    Gift_From_Others=models.IntegerField() 
    Agriculture_Income=models.IntegerField() 
    Casual_Income=models.IntegerField() 
    Other_Income_1=models.IntegerField()
    Other_Income_2=models.IntegerField()
    Other_Income_3=models.IntegerField()
    Income_from_other_Sources=models.IntegerField()

class Income_from_Business_Services_Profession(models.Model):
    GSTIN_No=models.CharField(max_length=50)
    GST_Sale_Amount_as_per_GST_Return=models.IntegerField()

class Business_of_transport(models.Model):
    Name_of_Business=models.CharField(max_length=100)
    Number_of_Vehicles=models.IntegerField()
    Vehicle_Registration_No=models.CharField(max_length=30)
    Vehicle_Type=models.CharField(max_length=1,choices=((1,'Owned'),(2,'Leased'),(3,'Hired')))
    Tonnage_Capacity_in_MT=models.IntegerField()
    Period_of_holding_in_month=models.IntegerField()
    Income_per_vehicle=models.IntegerField()
    Demeed_Income=models.IntegerField()
    Total_Demeed_Income=models.IntegerField()
    Partner_Member_own_capital=models.IntegerField()
    Secured_Loans=models.IntegerField()
    Unsecured_Loans=models.IntegerField()
    Advances=models.IntegerField()
    Sundry_Creditors=models.IntegerField()
    Other_Liabilities=models.IntegerField()
    Total_capital_and_liabilities=models.IntegerField()
    Fixed_Assests=models.IntegerField()
    Inventories=models.IntegerField()
    Sundry_Debtors=models.IntegerField()
    Balance_with_banks=models.IntegerField()
    Cash_in_hand=models.IntegerField()
    Loans_and_Advances=models.IntegerField()
    Other_Current_Assests=models.IntegerField()
    Total_Assests=models.IntegerField()

class Other_Business(models.Model):
    Business_Name=models.CharField(max_length=50)
  #######   that anoying large text # Types_of_Business=models.ForeignKey(Types_Of_Business,on_delete=models.CASCADE)
    Books_Maintained_or_not=models.CharField(max_length=1,choices=((1,'Yes'),(2,'No')))
    Cash_Sales_or_Receipts= models.IntegerField()
    Electronic_Sales_or_Receipts=models.IntegerField()
    Total_Gross_Sales_or_Receipt=models.IntegerField()
    Cash_Sales_Net_Profit_min_8_percent=models.IntegerField()
    Electronic_Sales_Net_Profit_min_6_percent=models.IntegerField()
    Income_Net_Profit_min_6_percent=models.IntegerField()
    Income_Net_Profit_in_percent=models.IntegerField()
    Opening_Stock=models.IntegerField()
    Purchase=models.IntegerField()
    Closing_Stock=models.IntegerField()
    Gross_Profit=models.IntegerField()
    Partner_members_own_capital=models.IntegerField()
    Secured_Loans=models.IntegerField()
    Unsecured_Loans=models.IntegerField()
    Advances=models.IntegerField()
    Sundry_Creditors=models.IntegerField()
    Other_Liability=models.IntegerField()
    Total_Capital_and_Liabilities=models.IntegerField()
    Fixed_Assests=models.IntegerField()
    Inventories_Closing_Stock=models.IntegerField()
    Sundry_Debtors=models.IntegerField()
    Balance_with_Banks=models.IntegerField()
    Cash_in_Hand=models.IntegerField()
    Loan_and_Advances=models.IntegerField()
    Other_Assests=models.IntegerField()
    Total_Assests=models.IntegerField()

class itr_products(models.Model):
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

  
