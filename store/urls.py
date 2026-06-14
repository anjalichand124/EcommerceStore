from django.urls import path
from . import views

urlpatterns = [

    # Home
    path('', views.home, name='home'),

    # Products
    path('products/', views.products, name='products'),

    # Product Detail
    path('product/<int:id>/', views.product_detail, name='product_detail'),

    # Cart
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:id>/', views.remove_from_cart, name='remove_from_cart'),

    # Quantity Buttons
    path(
        'cart/increase/<int:id>/',
        views.increase_quantity,
        name='increase_quantity'
    ),

    path(
        'cart/decrease/<int:id>/',
        views.decrease_quantity,
        name='decrease_quantity'
    ),

    # Order
    path('place-order/', views.place_order, name='place_order'),

    # Authentication
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]