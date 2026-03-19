from django.shortcuts import render, redirect
from .models import Product, Cart

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    Cart.objects.create(user=request.user, product=product)
    return redirect('home')

def cart(request):
    items = Cart.objects.filter(user=request.user)

    total = sum([item.total_price() for item in items])

    return render(request, 'store/cart.html', {
        'items': items,
        'total': total
    })