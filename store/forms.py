from django.forms import ModelForm
from .models import Product


class AddEditProduct(ModelForm):

    class Meta:

        model = Product
        fields = ["title", "description", "category", "price", "image"]
