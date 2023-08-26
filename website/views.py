from django.shortcuts import render
from .models import Phone

# Create your views here.
def home(request):
    context = {
        "tab":"home",
        "phones" : Phone.objects.all()
    }
    return render(request, "website/home.html", context)

def sales(request):
    context = {
        "tab":"sales",
    }
    return render(request, "website/sales.html", context)