def add_to_cart(request, id):
    cart = request.session.get('cart', {})

    id = str(id)

    if id in cart:
        cart[id] += 1
    else:
        cart[id] = 1

    request.session['cart'] = cart
    return redirect('/cart/')


def remove_from_cart(request, id):
    cart = request.session.get('cart', {})

    id = str(id)

    if id in cart:
        del cart[id]

    request.session['cart'] = cart
    return redirect('/cart/')