from django.db import models
from django.db import models 
# Create your models here.
class Detail(models.Model):
    product_name = models.CharField(max_length=200)
    type=models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    price=models.IntegerField()
    quantity=models.IntegerField()
    units=models.CharField(max_length=10,null=True)
    
class MessageForm(models.Model):
    Name=models.CharField(max_length=200)
    Email_id=models.CharField(max_length=200)
    Contact_no=models.IntegerField() 
    Message=models.TextField()    
    Date=models.DateTimeField(auto_now_add=True)
   
class FeedbackForm(models.Model):
    Name=models.CharField(max_length=200)
    Email_id=models.CharField(max_length=200)
    Contact_no=models.IntegerField() 
    Comment=models.TextField()    
    Date=models.DateTimeField(auto_now_add=True)    
    
class cart(models.Model):
    product_name=models.CharField(max_length=200)
    type=models.CharField(max_length=200)
    brand=models.CharField(max_length=200)
    price=models.IntegerField()
    quantity=models.IntegerField()
    units=models.CharField(max_length=10,null=True)
    image = models.ImageField(upload_to="grocery/uplo", default="")