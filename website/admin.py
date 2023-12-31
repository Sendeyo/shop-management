from django.contrib import admin
from .models import Product, Category, Sale


# Configure the Admin page
admin.site.site_header = "ERICO ELECTRONICS"
admin.site.index_title = ""
admin.site.site_title = "ERICO ELECTRONICS"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "quantity", "buyingPrice", "discountPrice","sellingPrice")
    list_filter = ["category"]
    search_fields = ["name", "description"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ["name"]


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity", "priceSold", "paymentMethod", "buyer", "seller", "dateTime", "status")
    list_filter = ["seller", "status", "paymentMethod", "dateTime"]
    search_fields = ["product", "buyer"]
    
















# Configure model looks from the db
class PhoneAdmin(admin.ModelAdmin):
    list_display = ("name", "model", "quantity", "buyingPrice", "sellingPrice")
    search_fields = ("name", "model", "screenSize")
    actions = ["culculate_discount", "out_of_stock"]

    def culculate_discount():
        pass

    def out_of_stock(self, request):
        pass

    culculate_discount.short_description = "Reculculate Discount"


class CaseAdmin(admin.ModelAdmin):
    list_display = ("phone","type", "quantity", "buyingPrice", "sellingPrice")
    list_filter = ["type"]
    # search_fields = ["type"]

    actions = ["clear_stock"]

    def clear_stock(self, request):
        # TODO 
        pass

class ProtectorAdmin(admin.ModelAdmin):
    list_display = ("phone","type", "quantity", "buyingPrice", "sellingPrice")
    list_filter = ["type"]
    # search_fields = ["type"]
    # ordering = ("some")


    actions = ["clear_stock"]

    def clear_stock(self, request):
        # TODO 
        pass




# Register your models here.
# admin.site.register(CaseType)
# admin.site.register(ProtectorType)
# admin.site.register(Case, CaseAdmin)
# admin.site.register(Protector, ProtectorAdmin)
# admin.site.register(Phone, PhoneAdmin)

