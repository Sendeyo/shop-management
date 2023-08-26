from django.contrib import admin
from .models import CaseType, ProtectorType, Case, Protector, Phone

# Configure the Admin page
admin.site.site_header = "ERICO ELECTRONICS"
admin.site.index_title = ""
admin.site.site_title = "ERICO ELECTRONICS"

# Configure model looks from the db
class PhoneAdmin(admin.ModelAdmin):
    list_display = ("name", "model", "quantity", "buyingPrice", "sellingPrice", "ram", "rom")
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


    actions = ["clear_stock"]

    def clear_stock(self, request):
        # TODO 
        pass


# Register your models here.
admin.site.register(CaseType)
admin.site.register(ProtectorType)
admin.site.register(Case, CaseAdmin)
admin.site.register(Protector, ProtectorAdmin)
admin.site.register(Phone, PhoneAdmin)