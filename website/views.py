from django.shortcuts import render
from django.contrib import messages
from .models import Product, Category, Sale
from users.models import Contact, Debt, Log
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
# paginator
from django.core.paginator import Paginator
import datetime

# Create your views here.
# 
@login_required
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
                log = f"Sold {quantity} -- {product.name} to {customer}"
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
                log = f"Sold {quantity} {product.name} to new Customer {newCustomer.phone}"
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
            newLog = Log(user = request.user, action = log)
            newLog.save()
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
            log = f"Sold {quantity} -- {product.name} to Anonymous Customer"
            messages.success(request, f"You have sold {product.name} to Anonymous Customer")
            newSale.save()
            newLog = Log(user = request.user, action = log)
            newLog.save()

        context = {
            "tab":"home",
            "products" : Product.objects.all(),
            "categories" : Category.objects.all(),
        }
        return render(request, "website/home.html", context)
    else:
        productsDb = Product.objects.all()
        pagination = Paginator(productsDb, 50)
        products = pagination.get_page(request.GET.get("page"))

        context = {
            "tab":"home",
            "products" : products,
            "categories" : Category.objects.all(),
        }
        return render(request, "website/home.html", context)
    
## Products Forms -----------------------------------------------------<
@login_required
def products(request):
    productsFromDb = Product.objects.all().order_by("-id")
    paginator = Paginator(productsFromDb, 20)
    products = paginator.get_page(request.GET.get("page"))

    context = {
        "tab":"settings", "subtab":"products",
        "form" : ProductForm,
        "products":products,
    }

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            log = f"Added {request.POST.get('quantity')}  {request.POST.get('name')} under {request.POST.get('category')}"
            Log(user = request.user, action = log).save()
            messages.success(request, "Product Added Successfully")
            context["form"] = form
            return render(request, "website/products.html", context)
        else:
            messages.warning(request, "Product addition Failed")
            return render(request, "website/products.html", context)
    return render(request, "website/products.html", context)


## Products Forms ----------------------------------------------------->
@login_required
def sales(request):
    salesDb = Sale.objects.all().order_by("-id")
    paginator = Paginator(salesDb, 10)
    sales = paginator.get_page(request.GET.get("page"))
    context = {
        "tab":"sales",
        "sales": sales
    }
    return render(request, "website/sales.html", context)

def cart(request):
    context = {
        "tab":"cart",
    }
    return render(request, "website/cart.html", context)

# Contact Views -----------------------------------------------------<
@login_required
def contact(request):
    contactsDB = Contact.objects.all().order_by("-id")
    paginator = Paginator(contactsDB, 20)
    contacts = paginator.get_page(request.GET.get("page"))
    context = {
        "tab":"settings",
        "subtab":"contact",
        "contacts": contacts,
    }
    return render(request, "website/contacts.html", context)

@login_required
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