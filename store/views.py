from django.shortcuts import render
from .models import Product


def home(request):
    return render(request, 'store/home.html')

def product_detail(request, product_id):
    details = Product.objects.get(id=product_id)
    context = {
        'details': details
    }
    return render(request, 'store/product_detail.html', context)