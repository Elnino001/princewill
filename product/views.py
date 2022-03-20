from django.shortcuts import render, get_object_or_404
from .models import Product
from cart.forms import CartAddProductForm

# Create your views here.
def product_list(request, category_slug=None):
    category = None
    products = Product.objects.filter(available=True)
    if category_slug:
        products = products.filter(category=category)
    return render(request,
    'product/list.html',
    {'category': category,
    'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'product/details.html', {'product': product, 'cart_product_form': cart_product_form})