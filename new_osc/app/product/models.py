from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(
        max_length = 30,
    )
    description = models.CharField(
        max_length = 50,
    )
    product_type = models.CharField(
        max_length = 50,
        choices = (
            ("M", "Male"),
            ("F", "Female"),
        ), 
    )
    size = models.CharField(
        max_length = 10,
        choices = (
            ("M", "M"),
            ("L", "L"),
            ("XL", "XL"),
            ("XXL", "XXL")
        ),
    )
    price = models.IntegerField()
    photo = models.FileField()

    cloth = models.CharField(
        max_length = 10,
        choices = (
            ("party", "party_wear"),
            ("casual", "casual_wear")
        )
    )

    color = models.CharField(
        max_length = 10,
        default= False,
        choices = (
            ("black", "Black"),
            ("white", "White"),
            ("red", "Red"),
            ("purple", "Purple"),
            ("blue", "Blue"),
            ("green", "Green"),
            ("navyblue", "Navyblue"),
            ("grey", "Grey"),
        )
    )

    vender = models.ForeignKey( 
        'vender.Vender',
        default = True,
        on_delete = models.CASCADE,
        related_name="vender",
        )