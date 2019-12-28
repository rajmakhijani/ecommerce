from django.db import models

# Create your models here.
class Vender(models.Model):
    name = models.CharField(
        null = False,
        max_length = 20
    )
    shop_name = models.CharField(
        max_length = 40
    )
    def __str__(self,*args,**kwargs):
       return self.shop_name

       
    contact_no = models.IntegerField(
        blank = False,

    )
    email = models.EmailField(
        default= False ,
    )
    address = models.CharField(
        max_length= 40,
        default= False
    )


