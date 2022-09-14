from django.db import models


# Create your models here.
class UserDetailsModel(models.Model):
   user_id=models.AutoField(primary_key=True)
   name=models.CharField(max_length=100)
   email=models.EmailField()
   phno=models.BigIntegerField()
   profile_photo=models.ImageField(upload_to='images/')   
   password=models.CharField(max_length=50)
   customer_cart_address=models.IntegerField(help_text='address_id',default=0)
   class Meta:
         db_table = 'user_details'
         
       