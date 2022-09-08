from django.contrib import admin
from .models import Profile,Product,Order
# Register your models here.




@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user","userType","phone","address")
    list_filter = ("user","userType","phone","address")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","stock","price")
    list_filter = ("name","stock","price")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer","product","orderStatus")
    list_filter = ("customer","product","orderStatus")