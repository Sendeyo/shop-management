from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home-page"),
    path("sales/", views.sales, name="sales-page"),
    path("contacts/", views.contact, name="contacts-page"),
    path("cart/", views.cart, name="cart-page"),
    path("products/", views.products, name="products-page"),
    ## forms
    path("addProduct/", views.addProduct, name="add-product-page"),
]