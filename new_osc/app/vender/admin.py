from django.contrib import admin
from .models import Vender

# Register your models here.
@admin.register(Vender)
class VenderAdmin(admin.ModelAdmin):
    list_display = ['name','contact_no','email','address','shop_name']
