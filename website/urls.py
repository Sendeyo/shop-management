from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home-page"),
    path("sales/", views.sales, name="sales-page"),
    path("contact/", views.contact, name="contact-page"),
    path("cart/", views.cart, name="cart-page"),
    path("products/", views.products, name="products-page"),
]