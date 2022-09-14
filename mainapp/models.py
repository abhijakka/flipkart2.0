from django.db import models
from sellerapp.models import *
from userapp.models import *

# Create your models here.
class CartModel(models.Model):
    cart_id=models.AutoField(primary_key=True)
    cart_owner=models.ForeignKey(UserDetailsModel,on_delete=models.CASCADE,null=True)
    cart_product=models.ForeignKey(ProductUploadModel,on_delete=models.CASCADE,null=True)
    cart_product_qty=models.CharField(help_text='product_quantity',max_length=50,default=1)
    cart_product_price=models.CharField(help_text='Prodcuts_price',max_length=50,null=True)

    class Meta:
        db_table='cart_details' 
        
        
class CustomerAddress(models.Model):
    address_id=models.AutoField(primary_key=True)
    landmark=models.CharField(max_length=200,help_text='landmark',null=True)
    city=models.CharField(max_length=200,null=True)
    zip_code=models.CharField(max_length=10,null=True)
    flat_no=models.CharField(max_length=100,null=True)
    address_type=models.CharField(max_length=100,null=True)
    contact_no=models.CharField(max_length=15,null=True)
    address_name=models.CharField(max_length=20,null=True)
    customer=models.ForeignKey(UserDetailsModel,on_delete=models.CASCADE)

    class Meta:
        db_table='customer_address'    


class OrdersModels(models.Model):
    order_id=models.AutoField(primary_key=True)
    order_unique_id=models.CharField(max_length=100,help_text='order_id_from_razorpay',null=True)
    order_payment_id=models.CharField(max_length=100,help_text='Payment_id_from_razorpay',null=True)
    order_customer=models.ForeignKey(UserDetailsModel,on_delete=models.CASCADE,related_name='user_orders')
    order_product=models.ForeignKey(ProductUploadModel,on_delete=models.CASCADE,null=True)
    order_product2=models.ForeignKey(ProductModel,on_delete=models.CASCADE,null=True)
    order_product_price=models.IntegerField(help_text='order_price',null=True)
    order_product_qty=models.IntegerField(help_text='order_product_qty',null=True)
    order_product_amount=models.IntegerField(help_text='order_product_amount',null=True)
    order_product_seller=models.ForeignKey(SellerDetailsModel,on_delete=models.CASCADE,related_name='seller_ordered_products',null=True)
    order_date=models.DateTimeField(auto_now=True,help_text='order_date')
    order_payment_status=models.CharField(max_length=20,help_text='payment_status',default='Pending')
    order_status=models.CharField(max_length=100,default='Pending',help_text='order_status')
    order_address=models.ForeignKey(CustomerAddress,models.SET_DEFAULT,related_name='order_address',null=True,default='null')
    landmark=models.CharField(max_length=200,help_text='landmark',null=True)
    city=models.CharField(max_length=200,null=True)
    zip_code=models.CharField(max_length=10,null=True)
    flat_no=models.CharField(max_length=100,null=True)
    contact_no=models.CharField(max_length=15,null=True)
    address_name=models.CharField(max_length=20,null=True)
    class Meta:
        db_table='order_details'  
        
class FeedbackModel(models.Model):
    feedback_id=models.AutoField(primary_key=True)
    feedback_message=models.CharField(max_length=200,help_text='feedback_message')
    feedback_rating=models.CharField(max_length=200,help_text='feedback_rating',null=True)
    feedback_sentiment=models.CharField(max_length=20,help_text='sentiment_analysis',null=True)
    feedback_customer=models.ForeignKey(UserDetailsModel,on_delete=models.CASCADE)
    feedback_product=models.ForeignKey(ProductUploadModel,on_delete=models.CASCADE)
    feedback_product2=models.ForeignKey(ProductModel,on_delete=models.CASCADE,null=True)
    feedback_seller=models.ForeignKey(SellerDetailsModel,on_delete=models.CASCADE)
    feedback_date=models.DateField(auto_now_add=True)
    feedback_time=models.TimeField(auto_now_add=True,null=True)

    class Meta:
        db_table='feedback_details'                   
        