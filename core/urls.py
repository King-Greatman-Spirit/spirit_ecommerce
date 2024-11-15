from django.urls import path
from .views import (
    checkout, 
    ItemDetailView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart
)

app_name = 'core'  # This app namespace allows you to refer to these URLs with the 'core:' prefix

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout', checkout, name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('a/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
]

