from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .forms import AddEditProduct
from django.contrib.auth.decorators import login_required


def home(request):
    categories = Category.objects.all()
    return render(request, "store/home.html", {"categories": categories})


def list_products(request, cat_slug):
    category = get_object_or_404(Category, title=cat_slug)
    products = category.related_products.all()
    return render(request, "store/list_products.html", {"products": products})


def product_detail(request, product_id):
    details = get_object_or_404(Product, id=product_id)
    context = {"details": details}
    return render(request, "store/product_detail.html", context)


@login_required
def add_edit_product(request, product_id=None):
    instance = None
    if product_id:
        instance = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = AddEditProduct(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddEditProduct(instance=instance)
    return render(request, 'store/add_edit_product.html', {'form': form})


@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    redirect("home")
