from distutils.command.upload import upload
import email
from django.db import models
from userapp.models import *
# Create your models here.
class SellerDetailsModel(models.Model):
     seller_id=models.AutoField(primary_key=True) 
     com_name=models.CharField(max_length=100)
     own_name=models.CharField(max_length=100)
     phno =models.BigIntegerField()
     email = models.EmailField()
     pancard = models.ImageField(upload_to='pancard/')
     com_logo = models.ImageField(upload_to='companylogo/')
     address_proof = models.ImageField(upload_to='addressproof/')
     address = models.CharField(max_length=100)
     password = models.CharField(max_length=50)
     status = models.CharField(max_length=40,default='pending')
     class Meta:
               db_table ='seller_details'
               
               
class ProductModel(models.Model):
     seller_id = models.ForeignKey(SellerDetailsModel,models.CASCADE,null=True)
     seller_name = models.CharField(max_length=100,default='name')   
     pro_id = models. AutoField(primary_key=True)
     catagory = models.CharField(max_length=50)
     pro_name = models.CharField(max_length=100)
     model_no = models.CharField(max_length=50)
     pro_prize = models.CharField(max_length=50)
     pro_discount = models.IntegerField(max_length=50,null=True)
     pro_image = models.ImageField(upload_to='product_image/') 
     discount_percentage = models.CharField(max_length=200,null=True) 
     description = models.CharField(max_length=200) 
     Product_uploaded_date= models.DateField(auto_now_add=True,null=True)
     purchasedcount=models.BigIntegerField(default=0,max_length=200,null=True)
     product_review=models.BigIntegerField(default=0,null=True)
     user_review_count=models.BigIntegerField(default=0,null=True)
     product_uploaded_status = models.CharField(max_length=200,null=True,default='pending')
     class Meta:
               db_table ='product_details'         
     
class ProductUploadModel(models.Model):
     product_id = models.AutoField(primary_key=True)
     seller_id = models.ForeignKey(SellerDetailsModel,models.CASCADE,null=True)
     pro_details = models.ForeignKey(ProductModel,on_delete=models.CASCADE,null=True) 
     product_name = models.CharField(max_length=50)
     product_images1 = models.ImageField(upload_to='productimages/',null=True)
     product_images2 = models.ImageField(upload_to='productimages/',null=True)
     product_images3 = models.ImageField(upload_to='productimages/',null=True)
     product_images4 = models.ImageField(upload_to='productimages/',null=True)
     product_images5 = models.ImageField(upload_to='productimages/',null=True)
     product_watchlist=models.ManyToManyField(UserDetailsModel,help_text='watchlist',blank=True,related_name='my_watchlist')
     purchasedcount=models.BigIntegerField(default=0,null=True)
     
     class Meta:
               db_table = 'product_photos_details'
                  
