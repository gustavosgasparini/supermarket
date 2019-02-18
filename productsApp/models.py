from django.db import models

# Create your models here.
class ProdType(models.Model):
    product_group = models.CharField(max_length=256)

    def __str__(self):
        return self.product_group


class Product(models.Model):
    product_code = models.IntegerField(unique=True, null=True)
    product_type = models.ForeignKey(ProdType, on_delete=models.PROTECT)
    product_name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    expiration_date = models.DateField()
    manufacture_date = models.DateField()
    description = models.TextField()
    photo = models.ImageField(upload_to='products_images', null=True)

    def __str__(self):
        return self.product_name