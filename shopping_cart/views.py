from django.shortcuts import render, redirect
from store.models import Product

def cart_home(request):
    cart = request.session.get('cart', {})

    products = []
    total = 0

    for id, qty in cart.items():
        product = Product.objects.get(id=id)
        product.qty = qty
        product.total_price = product.price * qty
        total += product.total_price
        products.append(product)

    return render(request, 'shopping_cart/cart.html', {
        'products': products,
        'total': total
    })


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    cart[str(product_id)] = cart.get(str(product_id), 0) + 1

    request.session['cart'] = cart
    return redirect('cart')