from django.urls import path
from cart.views import add_to_cart, cart, update_cart, success, checkout

urlpatterns = [
    path('cart', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('cart/success/', success, name='success'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('update_cart/<int:product_id>/', update_cart, name='update_cart'),
]