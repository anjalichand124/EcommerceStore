from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Product, Order


# HOME PAGE
def home(request):
    return render(request, 'store/home.html')


# PRODUCTS PAGE
def products(request):
    products = Product.objects.all()
    return render(request, 'store/products.html', {'products': products})


# CART PAGE
def cart(request):
    cart = request.session.get('cart', {})

    products = Product.objects.filter(id__in=cart.keys())

    cart_items = []
    total = 0

    for product in products:
        qty = cart[str(product.id)]
        item_total = product.price * qty
        total += item_total

        cart_items.append({
            'product': product,
            'qty': qty,
            'total': item_total
        })

    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'total': total
    })


# ADD TO CART
def add_to_cart(request, id):
    cart = request.session.get('cart', {})

    id = str(id)

    if id in cart:
        cart[id] += 1
    else:
        cart[id] = 1

    request.session['cart'] = cart

    return redirect('/cart/')


# REMOVE FROM CART
def remove_from_cart(request, id):
    cart = request.session.get('cart', {})

    id = str(id)

    if id in cart:
        del cart[id]

    request.session['cart'] = cart

    return redirect('/cart/')


# PRODUCT DETAIL PAGE
def product_detail(request, id):
    product = Product.objects.get(id=id)

    return render(
        request,
        'store/product_detail.html',
        {'product': product}
    )


# PLACE ORDER
def place_order(request):
    cart = request.session.get('cart', {})

    products = Product.objects.filter(id__in=cart.keys())

    total = 0

    for product in products:
        qty = cart[str(product.id)]
        total += product.price * qty

    Order.objects.create(
        customer_name="Customer",
        total_amount=total
    )

    request.session['cart'] = {}

    return render(
        request,
        'store/order_success.html'
    )


# REGISTER
def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect('/login/')

    return render(request, 'store/register.html')


# LOGIN
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('/products/')

    return render(request, 'store/login.html')


# LOGOUT
def logout_user(request):
    logout(request)
    return redirect('/')