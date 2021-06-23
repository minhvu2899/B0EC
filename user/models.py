from django.db import models
from django.contrib.auth.models import AbstractUser
from product.models import Product
from django.db.models.deletion import CASCADE
# Create your models here.



    
class CustomerUser(AbstractUser):
    phone_number =models.CharField(default='',max_length=15)
class Address(models.Model):
    user = models.ForeignKey(CustomerUser,on_delete=models.CASCADE)
    street =models.CharField(default='',max_length=255)
    apartment_number =models.CharField(default='',max_length=255)
    district=models.CharField(default='',max_length=255)
    city=models.CharField(default='',max_length=255)
    default=models.BooleanField(default=False)
    def ToString(self):
        return self.street+"," +self.apartment_number+","+self.district+","+ self.city

class Comment(models.Model):
    user = models.ForeignKey(CustomerUser,on_delete=models.CASCADE)
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField(default='')
    rating = models.IntegerField(default=0)
    order_id = models.IntegerField(default=0)
    create_at =models.DateTimeField(auto_now_add=True)
class Response(models.Model):
    employee = models.ForeignKey(CustomerUser,on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    response = models.TextField(default='')
    create_at =models.DateTimeField(auto_now_add=True)
class Wishlist(models.Model):
    user = models.ForeignKey(CustomerUser,on_delete=models.CASCADE)
    product= models.ForeignKey(Product, on_delete=models.CASCADE)

class CreditCard(models.Model):
    user = models.ForeignKey(CustomerUser,on_delete=models.CASCADE)
    name = models.TextField(default='')
    credit_card_number = models.TextField(default='')
    expiration_date = models.TextField(default='')
    cvv = models.TextField(default='')
    create_at =models.DateTimeField(auto_now_add=True)
    default=models.BooleanField(default=False)
    def formatNumber(self):
        number=''
        length= len(self.credit_card_number)
        for i in range(length-3):
            
            number+='*'
            if i%4 ==3:
                number+=' '
        number+= self.credit_card_number[length-3]
        number+= self.credit_card_number[length-2]
        number+= self.credit_card_number[length-1]
        return number

class RewardPoints(models.Model):
    user = models.ForeignKey(CustomerUser,on_delete=models.CASCADE)
    point = models.IntegerField(default=0)
    product_name = models.CharField(max_length=255)
    product_thumbnail = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
   