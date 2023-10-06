from django import forms
from django.forms import ModelForm
from .models import Product, Category

class ProductForm(ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(),label="", empty_label="Select Product Category", widget=forms.Select(attrs={"class": "form-control"}))
    class Meta:
        model = Product
        fields = "__all__"

        labels = {
            "name" : "",
            # "category" : "",
            "description" : "",
            "quantity" : "",
            "buyingPrice" : "",
            "sellingPrice" : "",
            "discountPrice" : "",
            "location" : "",
            }
        widgets = {
            "name" : forms.TextInput(attrs = {"class":"form-control", "placeholder":"Product Name"}),
            # "category": forms.Select(attrs = {"class":"form-control", "placeholder":"Select Category"}),
            "description" : forms.Textarea(attrs = {"class":"form-control", "placeholder":"Description"}),
            "quantity" : forms.NumberInput(attrs = {"class":"form-control", "placeholder":"Number of Units"}),
            "buyingPrice" : forms.NumberInput(attrs = {"class":"form-control", "placeholder":"Buying Price"}),
            "sellingPrice" : forms.NumberInput(attrs = {"class":"form-control", "placeholder":"Selling Price"}),
            "discountPrice" : forms.NumberInput(attrs = {"class":"form-control", "placeholder":"Discount"}),
            "location" : forms.Textarea(attrs = {"class":"form-control", "placeholder":"Placement Location"}),
        }
