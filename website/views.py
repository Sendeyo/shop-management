from django.shortcuts import render
from django.contrib import messages
from .models import Product, Category
from users.models import Contact, Debt
from .forms import ProductForm

# Create your views here.
# 
def home(request):
    if request.method == "POST":
        category = request.POST.get("category")
        search_value = request.POST.get("search_value")
        try:
            products = Product.objects.filter(
                category__name__icontains = category,
                name__icontains = search_value,
                )
            context = {
                "tab":"home",
                "products" : products,
                "categories" : Category.objects.all(),
                "selected_category": category,
                "search_value": search_value
                }
            return render(request, "website/home.html", context)
        except Exception as e:
            context = {
                "tab":"home",
                "products" : Product.objects.all(),
                "categories" : Category.objects.all(),
                }
            return render(request, "website/home.html", context)
    else:
        context = {
            "tab":"home",
            "products" : Product.objects.all(),
            "categories" : Category.objects.all(),

        }
        return render(request, "website/home.html", context)
    
## Products Forms -----------------------------------------------------<
def products(request):
    context = {
        "tab":"settings", "subtab":"products",
        "products": Product.objects.all(),
        "form" : ProductForm,
    }

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product Added Successfully")
            context["form"] = form
            return render(request, "website/products.html", context)
        else:
            messages.warning(request, "Product addition Failed")
            return render(request, "website/products.html", context)
    return render(request, "website/products.html", context)

def addProduct(request):
    context = {
        "tab":"settings",
        "subtab":"Add Product",
        "form" : ProductForm,
    }
    return render(request, "website/forms/addProduct.html", context)


## Products Forms ----------------------------------------------------->

def sales(request):
    context = {
        "tab":"sales",
    }
    return render(request, "website/sales.html", context)

def cart(request):
    context = {
        "tab":"cart",
    }
    return render(request, "website/cart.html", context)


def contact(request):
    context = {
        "tab":"settings",
        "subtab":"contact",
        "contacts": Contact.objects.all()
    }
    return render(request, "website/contacts.html", context)