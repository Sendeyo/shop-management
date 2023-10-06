from django.contrib import admin
from .models import Debt, Contact
# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "category","phone", "description")
    search_fields = ["name", "phone", "category"]
    list_filter = ["category"]




@admin.register(Debt)
class DebtAdmin(admin.ModelAdmin):
    list_display = ("contact", "amount", "category", "status", "description")
    list_filter = ("category", "status")
    search_fields = ["contact__name"]



# admin.site.register(Debt)
# admin.site.register(Contact)