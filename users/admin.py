from django.contrib import admin
from .models import Debt, Contact, Log
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



@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ("user", "dateTime", "action")
    list_filter = ("user", "dateTime")
# admin.site.register(Contact)