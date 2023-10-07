from django.shortcuts import render
from django.contrib import messages
from .models import Product, Category, Sale
from users.models import Contact, Debt
from .forms import ProductForm

import datetime

# Create your views here.
# 
def home(request):
    if request.method == "POST" and "searcher" in request.POST:
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
                "search_value": search_value,
                "a":100,
                "b":50,
                }
            return render(request, "website/home.html", context)
        except Exception as e:
            context = {
                "tab":"home",
                "products" : Product.objects.all(),
                "categories" : Category.objects.all(),
                }
            return render(request, "website/home.html", context)
    elif request.method == "POST" and "seller" in request.POST:
        product = Product.objects.get(pk=request.POST.get("product"))
        quantity = int(request.POST.get("quantity"))
        priceSold = product.sellingPrice if request.POST.get("priceSold")=="" else request.POST.get("priceSold")
        paymentMethod = request.POST.get("paymentMethod")
        status = request.POST.get("status")
        seller = request.user if request.user.is_authenticated else None
        buyerName = request.POST.get("buyerName") # not for sale
        buyerNumber = request.POST.get("buyerNumber") # not for sale

        errors = []
        # Ensure you are not giving more discount than allowed
        if product.sellingPrice - int(priceSold) > product.discountPrice:
            error = f"You cant sell {product.name} for less than {product.sellingPrice - product.discountPrice}"
            errors.append(error)

        # Ensure you are not selling the wrong number of products
        if quantity < 1 or quantity > product.quantity:
            if quantity == 0:
                message = "You cant sell 0 product"
                errors.append(message)
            elif quantity < 0:
                message = "You cant sell Negative Product"
                errors.append(message)
            else:
                message = f"You cant sell more than {product.quantity} {product}"
                errors.append(message)

        # Ensure the phone number is right
        if len(buyerNumber) < 10:
            message = f"That Phone Number is not Valid."
            errors.append(message)

        # Send the errors to the user
        if errors:
            for error in errors:
                messages.warning(request, error)
            context = {
            "tab":"home",
            "products" : Product.objects.all(),
            "categories" : Category.objects.all(),
            }
            return render(request, "website/home.html", context)

        product.quantity = product.quantity-quantity
        product.save() #Remaining Quantity update

        totalCost = priceSold * quantity
        if buyerNumber and len(buyerNumber) >=10:
            theNumber = buyerNumber[-9:]
            unknownCustomers= Contact.objects.filter(phone__icontains = theNumber)
            if unknownCustomers:
                customer = unknownCustomers[0]
                messages.success(request, f"You have sold {product.name} to {customer}")
            else:
                newCustomer = Contact(
                    name=buyerName if buyerName else None,
                    category = "customer",
                    phone = f"0{theNumber}",
                    description = f"Bought {product.name} on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} "
                )
                customer = newCustomer.save()
                customer = newCustomer
                messages.success(request, f"You have sold {product.name} to new Customer {newCustomer.phone}")
            newSale = Sale(
                product = product,
                quantity = quantity,
                priceSold = totalCost,
                paymentMethod = paymentMethod,
                buyer = customer,
                seller = seller,
                status = status
            )
            newSale.save()
        else:
            newSale = Sale(
                product = product,
                quantity = quantity,
                priceSold = totalCost,
                paymentMethod = paymentMethod,
                buyer = None,
                seller = seller,
                status = status
            )
            messages.success(request, f"You have sold {product.name} to Unknown Customer")

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
        "products": Product.objects.all().order_by("-id"),
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

## Products Forms ----------------------------------------------------->

def sales(request):
    context = {
        "tab":"sales",
        "sales": Sale.objects.all().order_by("-id")
    }
    return render(request, "website/sales.html", context)

def cart(request):
    context = {
        "tab":"cart",
    }
    return render(request, "website/cart.html", context)

# Contact Views -----------------------------------------------------<

def contact(request):
    context = {
        "tab":"settings",
        "subtab":"contact",
        "contacts": Contact.objects.all().order_by("-id")
    }
    return render(request, "website/contacts.html", context)

def contactDetails(request, pk):
    contact = Contact.objects.get(pk=pk)
    context = {
        "tab":"settings",
        "subtab":contact.name,
        "contact": contact,
        "sales" : Sale.objects.all().filter(buyer=pk).order_by("-id"),
        "debts" : Debt.objects.all().filter(contact=pk).order_by("-id"),
    }
    return render(request, "website/detailPage/contactDetails.html", context)



# Contact Views ----------------------------------------------------->