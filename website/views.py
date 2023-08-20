from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request, "website/home.html", context)

def sales(request):
    context = {}
    return render(request, "website/sales.html", context)