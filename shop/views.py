from django.shortcuts import render, redirect
from .models import Product, Order

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Эта функция будет защищена. Если пользователь не авторизован, он будет перенаправлен на страницу /login/
@login_required(login_url='//')  # Указываем URL страницы авторизации
def protected_page(request):
    return render(request, 'protected_page.html')


def index(request):
    return render(request, 'index.html')

def catalog(request):
    products = Product.objects.all()
    return render(request, 'shop/catalog.html', {'products': products})

def orders(request):
    if not request.user.is_authenticated:
        return redirect('auth:signin')
    orders = Order.objects.filter(user=request.user)
    return render(request, 'shop/orders.html', {'orders': orders})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})

def orders_create(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        Order.objects.create(
            user=request.user,
            product=product,
            delivery_address=request.POST.get('delivery_address')
        )
        return redirect('shop:orders')
    return render(request, 'shop/order_create.html', {'product': product})