from django.forms import ModelForm
from .models import Product

class ProductsForm(ModelForm):

    class Meta():
        model = Product
        fields = ['product_code', 'product_type', 'product_name', 'price', 'expiration_date', 'manufacture_date', 'description', 'photo']